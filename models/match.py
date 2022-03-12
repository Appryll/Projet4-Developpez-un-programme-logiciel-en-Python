class Match:

    def __init__(self, name, date_time_debut, date_time_fin):
        self.name = name
        self.date_time_debut = date_time_debut
        self.date_time_fin = date_time_fin
        self.rounds = []

    def set_rounds(self):
        """Return round list"""
        return [
            self.name,
            self.date_time_debut,
            self.date_time_fin,
            self.rounds
        ]

    def get_match_players(self, player_1, player_2):
        """Get match paring tuple"""

        match = (
            f"{player_1['nom']}, {player_1['prenom']}",
            player_1["ranking"],
            player_1["score"],
            f"{player_2['nom']}, {player_2['prenom']}",
            player_2["ranking"],
            player_2["score"]
        )
        self.rounds.append(match)
