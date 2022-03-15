class MenuViews:

    def __init__(self):
        pass

    @staticmethod
    def app_title():
        print("********************************")
        print("         TOURNOI SUISSE")
        print("********************************")

    @staticmethod
    def main_menu():
        print("\n" * 2 + "-=-=- MENU PRINCIPAL -=-=-\n")
        print("[1] Créer un nouveau tournoi")
        print("[2] Créer un nouveau player")
        print("[3] Resume tournoi")
        """ print("[E] Editer un joueur")"""
        print("[4] Rapports")
        print("[5] Quitter")

    @staticmethod
    def create_tournament_header():
        print("\n" * 3 + "*** NOUVEAU TOURNOI ***")

    @staticmethod
    def time_control_options():
        print("\nSélectionnez le contrôle du temps :")
        print("[1] Bullet")
        print("[2] Blitz")
        print("[3] Rapid")
        print("\n[back] Retour au menu principal")

    @staticmethod
    def review_tournament(info, players):
        """Display all input info to review before saving to database

        @param info: input info list
        @param players: list of selected players
        """
        print("\n\nNouveau tournoi créé :\n")
        print(f"{info[0].upper()}, {info[1].title()}", end=' | ')
        print(f"Description : {info[2]}", end=' | ')
        print("Rounds : 4", end=' | ')
        print(f"Contrôle du temps : {info[3]}")
        print("\nPlayers (8 total) :\n")

        for item in players:
            print(f"Player {players.index(item) + 1} : ", end='')
            print(f"{item['id']}", end=' | ')
            print(f"{item['nom']}, {item['prenom']}", end=' | ')
            print(f"{item['date de naissance']}", end=' | ')
            print(f"Ranking : {item['ranking']}")

        print("\nEnregistrer dans la base de données ? [y/n] ", end='')

    @staticmethod
    def tournament_saved():
        print("\nTournoi enregistré avec succès !")

    @staticmethod
    def start_tournament_prompt():
        print("\nCommencer le tournoi maintenant ? [y/n] ", end='')

    @staticmethod
    def select_players(players, player_number):
        """Display all players to select

        @param players: list of players
        @param player_number: number of current player for new tournament (if editing player == "")
        """
        print(f"\nSélectionner un joueur {player_number} :\n")
        for i in range(len(players)):
            print(f"[{players[i]['id']}]", end=' ')
            print(f"{players[i]['nom']}, {players[i]['prenom']}", end=" | ")
            print(f"{players[i]['sexe']} | {players[i]['date_naissance']}", end=" | ")
            print(f"Ranking: {players[i]['ranking']}")

        print("\n[back] Retour au menu principal")

    @staticmethod
    def select_tournament(tournaments):
        """Display all tournaments to select

        @param tournaments: tournaments list
        """
        print("\n" * 3 + "*** TOURNOI SÉLECTIONNÉ ***\n")

        for i in range(len(tournaments)):
            print(f"[{tournaments[i]['id_tournoi']}]", end=' ')
            print(tournaments[i]['nom_tournoi'], end=' | ')
            print(tournaments[i]['lieu'], end=" | ")
            print(tournaments[i]['description'], end=' | ')
            print(f"Debut: {tournaments[i]['date_time_debut']}", end=' | ')
            print(f"Fin: {tournaments[i]['date_time_fin']}", end=' | ')
            print(f"Round {tournaments[i]['current_round']-1}/{tournaments[i]['rounds_total']}")

        print("\n[back] Retour au menu principal")

    @staticmethod
    def create_new_player_header():
        print("\n" * 3 + "- NOUVEAU PLAYER -\n")

    @staticmethod
    def review_player(info):
        """Display all input info to review before saving to database

        @param info: player info list
        """
        print("\n" * 2 + "Nouveau joueur créé :\n")
        print(f"{info[0]}, {info[1]}", end=' | ')
        print(f"Date de naissance : {info[2]}", end=' | ')
        print(f"Sexe : {info[3]}", end=' | ')
        print(f"Rang : {info[4]}")
        print("\nEnregistrer dans la base de données ? [y/n] ", end='')

    @staticmethod
    def update_player_info(p, options):
        """Player info editing prompts

        @param p: currently edited player
        @param options: editable options
        """
        print("\n" * 2 + "*** UPDATE PLAYER INFO ***\n")
        print(f"Updating {p.nom}, {p.prenom}\n")
        for i in range(len(options)):
            print(f"[{i+1}] Update {options[i]}")

        print("\n[back] Retour au menu principal")

    @staticmethod
    def player_saved():
        print("\nPlayer enregistré avec succès !")

    @staticmethod
    def reports_menu():
        print("\n" * 3 + "*** REPPORTS ***\n")
        print("[1] Tous les players")
        print("[2] Players dans un tournoi")
        print("[3] Tous les tournois")
        print("[4] Tours dans un tournoi")
        print("[5] Matchs dans un tournoi")
        print("\n[back] Retour au menu principal")

    @staticmethod
    def reports_player_sorting():
        print("\n[1] Trier par nom")
        print("[2] Trier par rang")
        print("\n[back] Retour au menu principal")

    @staticmethod
    def input_prompt_text(option):
        print(f"\nEntrer {option} : |- [back] pour retourner au menu principal -| ", end='')

    @staticmethod
    def input_prompt():
        print("\nType [option] and press Enter : ", end='')

    @staticmethod
    def are_you_sure_exit():
        print("\nÊtes-vous sûr de vouloir quitter le programme ? [y/n] ", end='')

    @staticmethod
    def input_error():
        print("\nInput error, please enter a valid option.")

    @staticmethod
    def player_already_selected():
        print("\nPlayer déjà sélectionné. Veuillez sélectionner un autre player.")

    @staticmethod
    def other_report():
        print("\nSouhaitez-vous voir un autre rapport ? [y/n] ", end='')

    @staticmethod
    def update_rank():
        print("\nUpdate ranking ? [y/n] ", end='')

    @staticmethod
    def rank_update_header(player):
        print(f"\nUpdating {player.nom}, {player.prenom}")
