from tinydb import TinyDB


class Tournoi:

    def __init__(self, id_tournoi, nom, lieu, date, nombre_de_tours, tourneaus, description, controle_du_temps):
        self.id_tournoi = id_tournoi
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nombre_de_tours = 4
        self.tourneaus = tourneaus
        self.description = description
        self.controle_du_temps = controle_du_temps

    def serialize_tournoi(self):
        """Return serialized tournoi"""

        serialized_tournoi = {
            'id_tournoi': self.id_tournoi,
            'nom': self.nom,
            'lieu': self.lieu,
            'date': self.date,
            'nombre_tours': self.nombre_de_tours,
            'tourneaus': self.tourneaus,
            'description': self.description,
            'controle_du_temps': self.controle_du_temps
        }
        return serialized_tournoi

    def save_tournoi(self):
        """Save new tournoi to database"""

        tournoi_db = TinyDB('db/tournois.json')
        tournois_table = tournoi_db.table('tournoi')
        # tournois_table.truncate()  #  clear the table first
        tournois_table.insert(self.serialize_tournoi())
