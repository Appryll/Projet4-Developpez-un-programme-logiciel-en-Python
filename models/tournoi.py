from tinydb import TinyDB


class Tournoi:

    def __init__(self, id_tournoi, nom_tournoi, lieu, debut_date, fin_date, description, controle_du_temps,
                 match_en_cours, players, matchs, matchs_total=4):
        self.id_tournoi = id_tournoi
        self.nom_tournoi = nom_tournoi
        self.lieu = lieu
        self.debut_date = debut_date
        self.fin_date = fin_date
        self.description = description
        self.controle_du_temps = controle_du_temps
        self.match_en_cours = match_en_cours
        self.matchs_total = matchs_total
        self.players = players
        self.matchs = matchs
        self.tour_db = TinyDB('db/tournois.json')

    def serialize_tournoi(self):
        """Return serialized tournoi"""

        serialized_tournoi = {
            'id': self.id_tournoi,
            'nom': self.nom_tournoi,
            'lieu': self.lieu,
            'debut_date': self.debut_date,
            'fin_date': self.fin_date,
            'description': self.description,
            'controle_du_temps': self.controle_du_temps,
            'matchs_en_cours': self.match_en_cours,
            'matchs_total': self.matchs_total,
            'players': self.players,
            'matchs': self.matchs
        }
        return serialized_tournoi

    def sort_players_by_rank(self):
        """Sort players by rank (ascending)"""
        self.players = sorted(self.players, key=lambda x: x.get('ranking'))

    def sort_players_by_score(self):
        """Sort players by score (descending)"""
        self.players = sorted(self.players, key=lambda x: x.get('score'), reverse=True)

    def split_players(self):
        """Split player in 2 halves (top and bottom players)"""
        half = len(self.players) // 2
        return self.players[:half], self.players[half:]

    def merge_players(self, top_players, bottom_players):
        """Merge top and bottom players in order of matches

        @param top_players: top half of players (list)
        @param bottom_players: bottom half of players (list)
        """
        merged_players = []
        for i in range(len(self.players) // 2):
            merged_players.append(top_players[i])
            merged_players.append(bottom_players[i])

        self.players = merged_players

    def save_tournoi(self):
        """Save new tournament to database
        Set tournament ID as document ID
        """
        tournoi_table = self.tour_db
        self.id_tournoi = tournoi_table.insert(self.serialize_tournoi())
        tournoi_table.update({'id': self.id_tournoi}, doc_ids=[self.id_tournoi])

    def update_tournai(self):
        """Update tournament info (after each round) in database"""
        db = TinyDB('db/tournois.json')
        db.update({'matchs': self.matchs}, doc_ids=[self.id_tournoi])
        db.update({'players': self.players}, doc_ids=[self.id_tournoi])
        db.update({'matchs_en_cours': self.match_en_cours}, doc_ids=[self.id_tournoi])

    def update_timer(self, timer, info):
        """Update start or end timer of tournament

        @param timer: date and time info (str)
        @param info: start or end time (str)
        """
        db = self.tour_db
        db.update({info: timer}, doc_ids=[self.id_tournoi])

    @staticmethod
    def load_tournament():
        """Load tournament database

        @return: list of tournaments
        """
        db = TinyDB('db/tournois.json')
        db.all()
        tournois_list = []
        for item in db:
            tournois_list.append(item)

        return tournois_list
