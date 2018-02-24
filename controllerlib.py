from __future__ import unicode_literals
from __future__ import print_function
import random


class Action(object):

    ROCK = 1
    SCISSORS = 2
    PAPER = 3

    @staticmethod
    def get_action_name(action):
        return {
            Action.ROCK: "Rock",
            Action.SCISSORS: "Scissors",
            Action.PAPER: "Paper"
        }.get(action, "Unknown")


class Bot(object):

    """
        The bot player! Simulates a User player.
    """

    @staticmethod
    def action():
        # type: () -> int
        """ This method forces a bot to make action (PAPER, ROCK, SCISSORS) """
        return random.randrange(1, 4)


class Controller(object):

    """
        The game controller.
    """

    def __init__(self):
        self._player_wins = 0
        self._bot_wins = 0

    def __call__(self, players_action):
        self.process(players_action)

    @staticmethod
    def get_bots_action(player_action):
        # type: (int) -> int
        """ Invokes 'action' method of the Bot """
        bot_action = Bot.action()
        while bot_action == player_action:
            bot_action = Bot.action()
        return bot_action

    @staticmethod
    def player_won():
        """ Shows that player is a winner """
        print("Congratulations! You have won!")
        quit()

    @staticmethod
    def bot_won():
        """ Shows that bot has won """
        print("You lose!")
        quit()

    @staticmethod
    def get_modulo_action(bot_action):
        modulo = ((bot_action + 1) % 3)
        if modulo == 0:
            modulo += 1
        return modulo

    def process(self, player_action):
        if (
            not isinstance(player_action, int) or
            player_action not in [Action.ROCK, Action.SCISSORS, Action.PAPER]
        ):
            return print("Please check your code. You sent an incorrect action")
        self.check_winner(player_action)

    def check_winner(self, player_action):
        # type: (int) -> None
        """ Adds a point to a winner """
        bot_action = self.get_bots_action(player_action)
        player_modulo = player_action - 1
        if player_modulo == ((bot_action + 1) % 3):
            self._player_wins += 1
        elif player_modulo == (bot_action % 3):
            self._bot_wins += 1
        else:
            raise AttributeError("??? DRAW ???")
        self.check_wins()

    def check_wins(self):
        # type: () -> None
        """ Checks if someone has won. Doing nothing if no one has won """
        if self._player_wins > 1 and self._bot_wins == 0 or self._player_wins > 2:
            self.player_won()
        elif self._bot_wins > 1 and self._player_wins == 0 or self._bot_wins > 2:
            self.bot_won()


controller = Controller()
