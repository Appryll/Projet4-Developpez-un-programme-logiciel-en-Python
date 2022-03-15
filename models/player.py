from tinydb import TinyDB


class Player:

    def __init__(self, id_player, nom, prenom, date_naissance, sexe, ranking):
        self.id_player = id_player
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.ranking = ranking
        self.score = 0.0
        self.opponents = []

        self.player_db = TinyDB('db/players.json')

    def serialize_player(self):
        """Return serialized player info"""
        return {
            "id": self.id_player,
            "nom": self.nom,
            "prenom": self.prenom,
            "date_naissance": self.date_naissance,
            "sexe": self.sexe,
            "ranking": self.ranking,
            "score": self.score,
            "opponents": self.opponents
        }

    def save_player(self):
        """Save new player to database
        Set player ID as document ID
        """
        players_db = self.player_db
        self.id_player = players_db.insert(self.serialize_player())
        players_db.update({'id': self.id_player}, doc_ids=[self.id_player])

    def update_player(self, info, option):
        """Update player info (from user input) in database

        @param info: user input (str, or int inf "rank")
        @param option: update info category
        """
        db = self.player_db
        if option == "ranking":
            db.update({option: int(info)}, doc_ids=[self.id_player])
        else:
            db.update({option: info}, doc_ids=[self.id_player])

    @staticmethod
    def load_player():
        """Load player database

        @return: list of players
        """
        players_db = TinyDB('db/players.json')
        players_db.all()
        players = []
        for item in players_db:
            players.append(item)

        return players
