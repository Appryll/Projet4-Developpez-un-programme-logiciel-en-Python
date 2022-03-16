from prettytable import PrettyTable
from rich import print
from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({
    "info": "yellow",
    "option": "#85F4FF"
})
console = Console(theme=custom_theme)


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

        console.print("\n\n- FINAL SCORES -\n", style="underline bold")
        print(f"{t.nom_tournoi.upper()}, {t.lieu.title()} | Description : {t.description}")
        print(f"Debut : {t.debut_date} | Fin : {t.fin_date} | Time control : {t.controle_du_temps}\n")

        print(self.table)

    @staticmethod
    def round_header(t, debut_date):
        """Display tournament info as a round header

        @param t: current tournament
        @param debut_date: tournament start time (str)
        """
        print("\n\n")

        h_1 = f"{t.nom_tournoi.upper()}, {t.lieu.title()} | Description : {t.description}"
        h_2 = f"Debut : {t.debut_date} Fin : {t.fin_date} | Controle du temps : {t.controle_du_temps}\n"
        h_3 = f"- ROUND {t.match_en_cours}/{t.matchs_total} | {debut_date} -"

        print(h_1.center(100, " "))
        print(h_2.center(100, " "))
        print(h_3.center(100, " "))

    @staticmethod
    def round_over():
        console.print("\nRound terminé ? (Tapez ok)", style="info")
        console.print("Tapez [i]'back'[/i] pour retourner au menu principal")

    @staticmethod
    def score_options(match_number):
        print("\nMatch ", match_number)
        print('[0] Match null')
        print('[1] Player 1 gagnant')
        print('[2] Player 2 gagnant')
        console.print("\nTapez [i]'back'[/i] pour retourner au menu principal")

    @staticmethod
    def score_input_prompt():
        console.print('\nEntrez le score :', end=' ', style="option")
