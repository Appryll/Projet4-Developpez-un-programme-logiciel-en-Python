from datetime import datetime

from models.player import Player
from models.match import Match

from views.match import MatchViews
from views.menu import MenuViews


class TournoiController:

    def __init__(self):
        self.menu_view = MenuViews()
        self.match_view = MatchViews()

        self.timer = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def start_tournament(self, t):
        """Tournament (t) main structure
        Start from first round or resume tournament according to round number
        Set start and end timers and save to DB
        """
        if t.match_en_cours == 1:
            t.date = self.timer
            t.update_timer(t.date, 'start_date')

            self.first_round(t)
            t.match_en_cours += 1
            t.update_tournament_db()

            while t.match_en_cours <= t.matchs_total:
                self.next_rounds(t)
                t.match_en_cours += 1
                t.update_tournament_db()

        elif 1 < t.match_en_cours <= t.matchs_total:
            while t.match_en_cours <= t.matchs_total:
                self.next_rounds(t)
                t.match_en_cours += 1
                t.update_tournament()

            t.end_date = self.timer
            t.update_timer(t.end_date, 'end_date')
            self.tournament_end(t)

        elif t.match_en_cours > t.matchs_total:
            self.tournament_end(t)

    def first_round(self, t):
        """First round : top players vs. bottom players
        Get pairings and set round to save to DB"""
        r = Match("Round 1", self.timer, "TBD")
        t.sort_players_by_rank()
        top_players, bottom_players = t.split_players()
        self.match_view.round_header(t, r.date_time_debut)

        for i in range(t.matchs_total):
            r.get_match_players(top_players[i], bottom_players[i])
            top_players[i], bottom_players[i] = self.update_opponents(top_players[i], bottom_players[i])

        self.match_view.display_matches(r.rounds)

        self.match_view.round_over()
        self.menu_view.input_prompt()
        user_input = input().lower()
        scores_list = []

        if user_input == "ok":
            r.end_datetime = self.timer
            t.rounds.append(r.set_rounds())
            t.merge_players(top_players, bottom_players)

            self.end_of_round(scores_list, t)

        elif user_input == "back":
            self.back_to_menu()

    def next_rounds(self, t):
        """Next rounds : set possible pairings
        Get pairings and set round to save to DB"""
        r = Match(("Round " + str(t.match_en_cours)), self.timer, "TBD")
        t.sort_players_by_score()
        self.match_view.round_header(t, r.date_time_debut)

        available_list = t.players
        players_added = []

        k = 0
        while k < t.matchs_total:
            if available_list[1]["id"] in available_list[0]["opponents"]:
                try:
                    available_list, players_added = \
                        self.match_other_option(available_list, players_added, r)
                    t.players = players_added

                except IndexError:
                    available_list, players_added = \
                        self.match_first_option(available_list, players_added, r)
                    t.players = players_added

            elif available_list[1]["id"] not in available_list[0]["opponents"]:
                available_list, players_added = \
                    self.match_first_option(available_list, players_added, r)
                t.players = players_added

            k += 1

        self.match_view.display_matches(r.rounds)

        self.match_view.round_over()
        self.menu_view.input_prompt()
        user_input = input().lower()
        scores_list = []

        if user_input == "ok":
            r.end_datetime = self.timer
            t.rounds.append(r.set_rounds())
            self.end_of_round(scores_list, t)

        elif user_input == "back":
            self.back_to_menu()

    def match_first_option(self, available_list, players_added, r):
        """Main pairing option

        @param available_list: list of players not set in match for current round
        @param players_added: list of players already in match for current round
        @param r: current round
        @return: updated lists
        """
        r.get_match_players(available_list[0], available_list[1])
        available_list[0], available_list[1] = self.update_opponents(available_list[0], available_list[1])

        available_list, players_added = self.update_player_lists(
            available_list[0],
            available_list[1],
            available_list,
            players_added
        )

        return available_list, players_added

    def match_other_option(self, available_list, players_added, r):
        """Alternative pairing option

        @param available_list: list of players not set in match for current round
        @param players_added: list of players already in match for current round
        @param r: current round
        @return: updated lists
        """
        r.get_match_players(available_list[0], available_list[2])
        available_list[0], available_list[2] = self.update_opponents(available_list[0], available_list[2])

        available_list, players_added = self.update_player_lists(
            available_list[0],
            available_list[2],
            available_list,
            players_added
        )

        return available_list, players_added

    def end_of_round(self, scores_list: list, t):
        """End of round : update player scores

        @param t: current tournament
        @param scores_list: list of scores
        @return: players list with updated scores
        """
        for i in range(t.matchs_total):
            self.match_view.score_options(i + 1)
            response = self.input_scores()
            scores_list = self.get_score(response, scores_list)

        t.players = self.update_scores(t.players, scores_list)

        return t.players

    def input_scores(self):
        """Score input"""
        self.match_view.score_input_prompt()
        response = input()
        return response

    def get_score(self, response, scores_list: list):
        """Input scores for each match in current round

        @param response: user input (str)
        @param scores_list: list of scores
        @return: updated list of scores
        """
        if response == "0":
            scores_list.extend([0.5, 0.5])
            return scores_list
        elif response == "1":
            scores_list.extend([1.0, 0.0])
            return scores_list
        elif response == "2":
            scores_list.extend([0.0, 1.0])
            return scores_list
        elif response == "back":
            self.back_to_menu()
        else:
            self.menu_view.input_error()
            self.input_scores()

    @staticmethod
    def update_scores(players, scores_list: list):
        """Update player scores

        @param players: list of players
        @param scores_list: list of scores
        @return: list of players with updated scores
        """
        for i in range(len(players)):
            players[i]["score"] += scores_list[i]

        return players

    @staticmethod
    def update_player_lists(player_1, player_2, available_list, players_added):
        """Update player lists :
        Add unavailable player to respective list
        Remove available player form respective list

        @param player_1: player 1 (dict)
        @param player_2: player 2 (dict)
        @param available_list: list of players not set in match for current round
        @param players_added: list of players already in match for current round
        @return: list of available players, list of unavailable players
        """
        players_added.extend([player_1, player_2])
        available_list.remove(player_1)
        available_list.remove(player_2)

        return available_list, players_added

    @staticmethod
    def update_opponents(player_1, player_2):
        player_1["opponents"].append(player_2["id"])
        player_2["opponents"].append(player_1["id"])

        return player_1, player_2

    def tournament_end(self, t):
        """End of tournament : display final results
        Offer user to update ranks

        @param t: current tournament dict
        """
        t.sort_players_by_rank()
        t.sort_players_by_score()

        self.match_view.display_results(t)

        self.menu_view.update_rank()
        user_input = input()

        players = t.players

        if user_input == "n":
            self.back_to_menu()

        elif user_input == "y":
            while True:
                self.update_ranks(players)

    def update_ranks(self, players):
        """Update player ranks and save to DB

        @param players: tournament player list
        """
        self.menu_view.select_players(players, "to update")
        self.menu_view.input_prompt()
        user_input = input()

        if user_input == "back":
            self.back_to_menu()

        for i in range(len(players)):
            if int(user_input) == players[i]["id"]:
                p = players[players.index(players[i])]
                p = Player(
                    p['id_player'],
                    p['nom'],
                    p['prenom'],
                    p['date_naissance'],
                    p['sexe'],
                    p['ranking']
                )

                self.menu_view.rank_update_header(p)
                self.menu_view.input_prompt_text("new ranking")
                user_input = input()

                if user_input == "back":
                    self.back_to_menu()

                else:
                    p.update_player(int(user_input), "ranking")
                    players[i]["ranking"] = int(user_input)

                    return players

    @staticmethod
    def back_to_menu():
        from controllers.menu import MenuControllers
        MenuControllers().main_menu_start()
