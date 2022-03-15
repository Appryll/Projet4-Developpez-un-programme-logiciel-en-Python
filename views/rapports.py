from prettytable import PrettyTable


class RapportsViews:

    def __init__(self):

        self.table = PrettyTable()

        self.player_report_field_names = [
            "Id",
            "Nom",
            "Prenom",
            "Sexe",
            "Date de naissance",
            "Ranking"
        ]

        self.tournament_report_field_names = [
            "Id",
            "Nom",
            "Lieu",
            "Description",
            "Date et heure de début",
            "Date et heure de fin",
            "Contrôle du temps",
            "Tournées",
            "Joueurs (ID : Name)",
        ]

        self.matches_report_field_names = [
            "Nom P1",
            "Ranking P1",
            "Score P1",
            " ",
            "Nom P2",
            "Ranking P2",
            "Score P2"
        ]

        self.rounds_report_field_names = [
            "Round #",
            "Debut le",
            "Fin le",
            "Matches"
        ]

    def display_players(self, players, sorting):
        """Display player report (all sorting types)"""
        self.table.clear()
        self.table.field_names = self.player_report_field_names
        self.table.align = "l"

        for i in range(len(players)):
            self.table.add_row([
                players[i]["id"],
                players[i]["nom"],
                players[i]["prenom"],
                players[i]["sexe"],
                players[i]["date_naissance"],
                players[i]["ranking"]
            ])

        print(f"\n\n\n- All players ({sorting}) -\n")
        print(self.table)

    def display_tournaments_report(self, tournaments):
        """Display tournament reports"""
        self.table.clear()
        self.table.field_names = self.tournament_report_field_names
        self.table.align = "l"

        for i in range(len(tournaments)):
            participants = []
            players = tournaments[i]["players"]
            for k in range(len(players)):
                participants.append(
                    str(players[k]["id"]) + " : " + players[k]["nom"])

            self.table.add_row([
                tournaments[i]["id"],
                tournaments[i]["nom"],
                tournaments[i]["lieu"],
                tournaments[i]["description"],
                tournaments[i]["date"],
                tournaments[i]["controle_du_temps"],
                str(tournaments[i]["current_round"]-1) + "/" + str(tournaments[i]["rounds_total"]),
                participants
            ])

        print("\n\n\n- All tournaments -\n")
        print(self.table)

    def display_matches_report(self, matches):
        """Display matches in tournament report"""
        self.table.clear()
        self.table.field_names = self.matches_report_field_names
        self.table.align = "l"

        for i in range(len(matches)):
            matches[i].insert(3, "vs.")
            self.table.add_row(matches[i])

        print(f"\n\n- All played matches ({len(matches)} total) -\n")
        print(self.table)

    def display_rounds_report(self, rounds):
        """Display rounds in tournament report"""
        self.table.clear()
        self.table.field_names = self.rounds_report_field_names
        self.table.align = "l"

        for i in range(len(rounds)):
            for j in range(4):
                if j == 0:
                    self.table.add_row([
                        rounds[i][0],
                        rounds[i][1],
                        rounds[i][2],
                        rounds[i][3][j]
                    ])
                else:
                    self.table.add_row([
                        ' ',
                        ' ',
                        ' ',
                        rounds[i][3][j]
                    ])

        print("\n\n- All played rounds -\n")
        print(self.table)

    @staticmethod
    def report_header(info):
        """Header for tournament reports

        @param info: tournament (dict)
        """
        print("\n\n")

        h_1 = f"{info['nom_tournoi'].upper()}, {info['lieu'].title()} | Description : {info['description']}"
        h_2 = \
            f"Date : {info['date']} | " \
            f"Contrôle du temps : {info['controle_du_temps']} | " \
            f"Tour joué : {info['matchs_en_cours']-1}/{info['matchs_total']}"

        print(h_1)
        print(h_2)
