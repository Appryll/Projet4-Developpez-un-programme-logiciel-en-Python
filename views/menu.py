from rich import print
from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({
    "info": "yellow",
    "title_ppal": "bold magenta",
    "title": "bold #FFC600",
    "subtitle": "bold #EF2F88",
    "danger": "bold red on white",
    "succes": "bold green",
    "option": "#85F4FF"
})
console = Console(theme=custom_theme)


class MenuViews:

    def __init__(self):
        pass

    @staticmethod
    def app_title():

        console.print("********************************", style="title_ppal")
        console.print("         TOURNOI SUISSE", style="title_ppal")
        console.print("********************************", style="title_ppal")

    @staticmethod
    def main_menu():
        console.print("\n" * 2 + "-=-=- MENU PRINCIPAL -=-=-\n", style="title")
        print("[1] Créer un nouveau tournoi")
        print("[2] Créer un nouveau player")
        print("[3] Resume tournoi")
        """ print("[E] Editer un joueur")"""
        print("[4] Rapports")
        print("[5] Quitter")
        console.print("\n" + "([u]Attention![/u] S'il n'y a pas de joueurs chargés dans la base de données," + "\n" +
                      "veuillez bien d'abord commencer par ajouter les données du joueur)", style="italic #D1D1D1")

    @staticmethod
    def create_tournament_header():
        console.print("\n" * 3 + "*** NOUVEAU TOURNOI ***", style="subtitle")

    @staticmethod
    def time_control_options():
        print("\nSélectionnez le contrôle du temps :")
        print("[1] Bullet")
        print("[2] Blitz")
        print("[3] Rapid")
        console.print("\n(Tapez [i]'back'[/i] pour retourner au menu principal)")

    @staticmethod
    def review_tournament(info, players):
        """Display all input info to review before saving to database

        @param info: input info list
        @param players: list of selected players
        """
        console.print("\n\nNouveau tournoi créé :\n", style="succes")
        print(f"{info[0].upper()}, {info[1].title()}", end=' | ')
        print(f"Description : {info[2]}", end=' | ')
        print("Rounds : 4", end=' | ')
        print(f"Contrôle du temps : {info[3]}")
        print("\nPlayers (8 total) :\n")

        for item in players:
            print(f"Player {players.index(item) + 1} : ", end='')
            print(f"{item['id']}", end=' | ')
            print(f"{item['nom']}, {item['prenom']}", end=' | ')
            print(f"{item['date_naissance']}", end=' | ')
            print(f"Ranking : {item['ranking']}")

        console.print("\nEnregistrer dans la base de données ? (y/n) ", end='', style="info")

    @staticmethod
    def tournament_saved():
        console.print("\nTournoi enregistré avec succès !", style="succes")

    @staticmethod
    def start_tournament_prompt():
        console.print("\nCommencer le tournoi maintenant ? (y/n) ", end='', style="info")

    @staticmethod
    def select_players(players, player_number):
        """Display all players to select

        @param players: list of players
        @param player_number: number of current player for new tournament (if editing player == "")
        """
        print(f"\nSélectionnez un joueur {player_number} :\n")
        for i in range(len(players)):
            print(f"[{players[i]['id']}]", end=' ')
            print(f"{players[i]['nom']}, {players[i]['prenom']}", end=" | ")
            print(f"{players[i]['sexe']} | {players[i]['date_naissance']}", end=" | ")
            print(f"Ranking: {players[i]['ranking']}")

        console.print("\n(Tapez [i]'back'[/i] pour retourner au menu principal)")

    @staticmethod
    def select_tournament(tournaments):
        """Display all tournaments to select

        @param tournaments: tournaments list
        """
        console.print("\n" * 3 + "*** TOURNOI SÉLECTIONNÉ ***\n", style="subtitle")

        for i in range(len(tournaments)):
            print(f"[{tournaments[i]['id']}]", end=' ')
            print(tournaments[i]['nom'], end=' | ')
            print(tournaments[i]['lieu'], end=" | ")
            print(tournaments[i]['description'], end=' | ')
            print(f"Debut: {tournaments[i]['debut_date']}", end=' | ')
            print(f"Fin: {tournaments[i]['fin_date']}", end=' | ')
            print(f"Round {tournaments[i]['matchs_en_cours']-1}/{tournaments[i]['matchs_total']}")

        console.print("\n(Tapez [i]'back'[/i] pour retourner au menu principal)")

    @staticmethod
    def create_new_player_header():
        console.print("\n" * 3 + "*** NOUVEAU PLAYER ***\n", style="subtitle")

    @staticmethod
    def review_player(info):
        """Display all input info to review before saving to database

        @param info: player info list
        """
        console.print("\n" * 2 + "Nouveau joueur créé :\n", style="succes")
        print(f"{info[0]}, {info[1]}", end=' | ')
        print(f"Date de naissance : {info[2]}", end=' | ')
        print(f"Sexe : {info[3]}", end=' | ')
        print(f"Rang : {info[4]}")
        console.print("\nEnregistrer dans la base de données ? (y/n) ", end='', style="info")

    @staticmethod
    def update_player_info(p, options):
        """Player info editing prompts

        @param p: currently edited player
        @param options: editable options
        """
        console.print("\n" * 2 + "*** UPDATE PLAYER INFO ***\n", style="subtitle")
        console.print(f"Updating {p.nom}, {p.prenom}\n", style="succes")
        for i in range(len(options)):
            print(f"[{i+1}] Update {options[i]}")

        console.print("\n(Tapez [i]'back'[/i] pour retourner au menu principal)")

    @staticmethod
    def player_saved():
        console.print("\nPlayer enregistré avec succès !", style="succes")

    @staticmethod
    def reports_menu():
        console.print("\n" * 3 + "*** REPPORTS ***\n", style="subtitle")
        print("[1] Tous les players")
        print("[2] Players dans un tournoi")
        print("[3] Tous les tournois")
        print("[4] Tours dans un tournoi")
        print("[5] Matchs dans un tournoi")
        print("\n(Tapez [i]'back'[/i] pour retourner au menu principal)")

    @staticmethod
    def reports_player_sorting():
        print("\n[1] Trier par nom")
        print("[2] Trier par rang")
        console.print("\n(Tapez [i]'back'[/i] pour retourner au menu principal)")

    @staticmethod
    def input_prompt_text(option):
        console.print(f"\nEntrer {option} : (Tapez [i]'back'[/i] pour retourner au menu principal)  ", end='')

    @staticmethod
    def input_prompt():
        console.print("\nTapez l'option et pressez Enter SVP : ", end='', style="option")

    @staticmethod
    def are_you_sure_exit():
        console.print("\nÊtes-vous sûr de vouloir quitter le programme ? (y/n) ", end='', style="info")

    @staticmethod
    def input_error():
        console.print("\nInput error, please enter a valid option.", style="danger")

    @staticmethod
    def player_already_selected():
        console.print("\nPlayer déjà sélectionné. Veuillez sélectionner un autre player.", style="danger")

    @staticmethod
    def other_report():
        console.print("\nSouhaitez-vous voir un autre rapport ? (y/n) ", end='', style='info')

    @staticmethod
    def update_rank():
        console.print("\nUpdate ranking ? (y/n) ", end='', style='info')

    @staticmethod
    def rank_update_header(player):
        console.print(f"\nUpdating {player.nom}, {player.prenom}", style="succes")
