#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for Joe Chan: assignment7.py."""


import argparse
import random
random.seed(0)


class Dice(object):
    """A dice object class definition."""

    def __init__(self):
        """Constructor for the dice() class."""
        self.result = 0

    def roll_dice(self):
        """Assigns a random number to the dice() object."""
        self.result = random.randint(1, 6)
        print "You have rolled a: ", str(self.result)
        return self.result

    def reset(self):
        """Assigns a zero to the result attribute of the dice() object."""
        self.result = 0


class Player(object):
    """A Player class definition."""

    def __init__(self, numID):
        """Constructor for the Player() class."""
        self.id = str(numID + 1)
        self.totalscore = 0

    def reset(self):
        """Resets the totalscore attribute to zero."""
        self.totalscore = 0

    def get_id(self):
        """Returns the id attribute."""
        return self.id

    def get_totalscore(self):
        """Returns the totalscore attribute."""
        return self.totalscore

    def print_totalscore(self):
        """Prints the totalscore attribute."""
        print "*Your Score is:", str(self.totalscore)
        return

    def getTempTotal(self, tempscore):
        """Calculates a temporary total score for the round."""
        return (self.totalscore + tempscore)

    def add_round_score(self, roundscore):
        """Updates the totalscore with the roundscore."""
        self.totalscore = self.totalscore + roundscore
        return


class PIGSgame(object):
    """A PIGS game class definition."""

    def __init__(self, num=2):
        """Constructor for the PIGSgame() class.

        Args:
            num(integer): The number of players in the game. Default: 2

        Attributes:
            mydice (object): The dice() object.
            endgame (boolean): A boolean to determine if the game continues on.
            player_list (list): A list of Player() objects.
        """
        self.mydice = Dice()
        endgame = False

        player_list = [None] * num
        for a in range(num):
            player_list[a] = Player(a)

        while not endgame:
            for b in range(num):
                endgame = self.play_round(player_list[b])
                if endgame is True:
                    break

        self.mydice.reset()
        for c in range(num):
            player_list[c].reset()

    def play_round(self, gameplayer):
        """A function that rolls the dice and prints the round score.

        Args:
            gameplayer(object): The Player() object.

        Attributes:
            temp_player (string): The id of the Player() object.
            score (integer): The score based on the dice() object.
            round_score (integer): The total round score.
            endgame, endturn (boolean): A boolean to continue the loop.
        """
        temp_player = gameplayer.get_id()
        round_score = 0
        endgame = False
        endturn = False
        print "Player:", temp_player + "'s turn to roll."
        while not endturn and not endgame:
            gameplayer.print_totalscore()
            answer = raw_input("Type R to ROLL the dice or H to HOLD: ")
            if answer.lower() == "r":
                score = self.mydice.roll_dice()
                if score == 1:
                    print "Sorry, You have lost your turn!"
                    gameplayer.print_totalscore()
                    print "-------------------------"
                    round_score = 0
                    endturn = True
                else:
                    round_score = round_score + score
                    print "*Your Current Round Score is:", str(round_score)
                    temp_total = gameplayer.getTempTotal(round_score)
                    if temp_total >= 100:
                        gameplayer.add_round_score(round_score)
                        gameplayer.print_totalscore()
                        print "Congratulations! "
                        print "Player:", temp_player + " is the Winner!"
                        endgame = True
            elif answer.lower() == "h":
                print "You have selected to hold"
                gameplayer.add_round_score(round_score)
                gameplayer.print_totalscore()
                print "-------------------------"
                endturn = True
            else:
                print "Error: Please select R or H."

        return endgame


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enter the number of players:")
    parser.add_argument("-n", "--numPlayers", help="Enter the number of players"
                        , type=int)
    args = parser.parse_args()

    if args.numPlayers:
        numPlayers = args.numPlayers
        if numPlayers > 1:
            PIGSgame(numPlayers)
