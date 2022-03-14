from tinydb import TinyDB


class Tournoi:

    def __init__(self, id_tournoi, nom_tournoi, lieu, date, nombre_de_tours, tourneaus, description, controle_du_temps,
                 match_en_cours, matchs_total, players, matchs):
        self.id_tournoi = id_tournoi
        self.nom_tournoi = nom_tournoi
        self.lieu = lieu
        self.date = date
        self.nombre_de_tours = 4
        self.tourneaus = tourneaus
        self.description = description
        self.controle_du_temps = controle_du_temps
        self.match_en_cours = match_en_cours
        self.matchs_total = matchs_total
        self.players = players
        self.matchs = matchs

    def serialize_tournoi(self):
        """Return serialized tournoi"""

        serialized_tournoi = {
            'id_tournoi': self.id_tournoi,
            'nom': self.nom_tournoi,
            'lieu': self.lieu,
            'date': self.date,
            'nombre_tours': self.nombre_de_tours,
            'tourneaus': self.tourneaus,
            'description': self.description,
            'controle_du_temps': self.controle_du_temps,
            'matchs_en_cours': self.match_en_cours,
            'matchs_total': self.matchs_total,
            'players': self.players,
            'matchs': self.matchs
        }
        return serialized_tournoi

    def save_tournoi(self):
        """Save new tournoi to database"""

        tournoi_db = TinyDB('db/tournois.json')
        tournois_table = tournoi_db.table('tournoi')
        # tournois_table.truncate()  #  clear the table first
        tournois_table.insert(self.serialize_tournoi())

    @staticmethod
    def load_tournament():
        """Load tournament database

        @return: list of tournaments
        """
        db = TinyDB('db/tournaments.json')
        db.all()
        tournois_list = []
        for item in db:
            tournois_list.append(item)

        return tournois_list

    def update_tournai(self):
        """Update tournament info (after each round) in database"""
        db = TinyDB('db/tournois.json')
        db.update({'rounds': self.matchs}, doc_ids=[self.id_tournoi])
        db.update({'players': self.players}, doc_ids=[self.id_tournoi])
        db.update({'current_round': self.match_en_cours}, doc_ids=[self.id_tournoi])
