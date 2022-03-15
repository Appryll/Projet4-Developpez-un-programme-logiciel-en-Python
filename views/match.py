from prettytable import PrettyTable


class MatchViews:

    def __init__(self):
        self.table = PrettyTable()

        self.round_field_names = [
            "Match #",
            "Nom P1",
            "Ranking P1",
            "Score P1",
            " ",
            "Nom P2",
            "Ranking P2",
            "Score P2"
        ]

        self.results_field_names = [
            "Tournament ranking",
            "Nom",
            "Final Score",
            "Global ranking"
        ]

    def display_matches(self, rounds):
        """Display matches for current round as table

        @param rounds: list of matches tuples
        """
        self.table.clear()
        self.table.field_names = self.round_field_names

        for i in range(len(rounds)):
            row = list(rounds[i])
            row.insert(0, str(i+1))
            row.insert(4, "vs.")

            self.table.add_row(row)

        print(self.table)

    def display_results(self, t):
        """Display results at the end of the tournament

        @param t: current tournament
        """
        self.table.clear()
        self.table.field_names = self.results_field_names

        for i in range(len(t.players)):
            self.table.add_row([
                i+1,
                t.players[i]["nom"] + ", " + t.players[i]["prenom"],
                t.players[i]["score"],
                t.players[i]["ranking"]
            ])

        print("\n\n- FINAL SCORES -\n")
        print(f"{t.nom.upper()}, {t.location.title()} | Description : {t.description}")
        print(f"Debut : {t.date_time_debut} | Fin : {t.date_time_fin} | Time control : {t.controle_du_tempsl}\n")

        print(self.table)

    @staticmethod
    def round_header(t, date_time_debut):
        """Display tournament info as a round header

        @param t: current tournament
        @param date_time_debut: tournament start time (str)
        """
        print("\n\n")

        h_1 = f"{t.nom.upper()}, {t.location.title()} | Description : {t.description}"
        h_2 = f"Date-time debut : {t.date_time_debut} | Controle du temps : {t.controle_du_temps}\n"
        h_3 = f"- ROUND {t.match_en_cours}/{t.matchs_totall} | {date_time_debut} -"

        print(h_1.center(100, " "))
        print(h_2.center(100, " "))
        print(h_3.center(100, " "))

    @staticmethod
    def round_over():
        print("\nRound over ? [ok]")
        print("Back to main menu ? [back]")

    @staticmethod
    def score_options(match_number):
        print("\nMatch ", match_number)
        print('[0] Match null')
        print('[1] Player 1 gagnant')
        print('[2] Player 2 gagnant')
        print("\n[back] Back to main menu")

    @staticmethod
    def score_input_prompt():
        print('\nEnter result :', end=' ')
