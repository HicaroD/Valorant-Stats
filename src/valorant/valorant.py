from extractor import WebExtractor, PlayerInfoExtractor
from bs4 import BeautifulSoup as bs4
import requests

class ValorantPlayer:
    def __init__(self, nickname, tag):
        self.nickname = nickname
        self.tag = tag
        self.player_info = PlayerInfoExtractor(self.nickname, self.tag)

    def _individual_performance(self, index):
        return self.player_info.get_individual_performance()[index]

    def kills(self):
        """Returns an string containing the amount of kills you have"""
        return self._individual_performance(8)

    def deaths(self):
        """Returns a integer string containing the amount of times you died"""
        return self._individual_performance(10)

    def assistances(self):
        """Returns a string containing the amount of assistances you have"""
        return self._individual_performance(11)

    def kills_per_round(self):
        """Returns a string containing the amount of kills per round (KPR) you have"""
        return self._individual_performance(-4)

    def damage_per_round(self):
        """Returns a string containing the amount of damage per round (DPR) you have"""
        return self._individual_performance(3)

    def headshot_percentage(self):
        """Returns a string containing the amount of damage per round (DPR) you have"""
        return self._individual_performance(5)

    def clutchs(self):
        """Returns a string containing the amount of clutchs you won"""
        return self._individual_performance(-3)

    def headshot_amount(self):
        """Returns a string containing the amount of kills (with headshots)"""
        return self._individual_performance(9)

    def rating(self):
        """Returns a string containing your rating (like Bronze, Silver or Radiant)"""
        return self.player_info.get_player_rating()

    def top_weapon(self):
        """Returns a dictionary containing informations about your top weapon.\n You can access the info with these keys below: Weapons, Headshots, Bodyshot, Leg_shot, Kills"""
        return self.player_info.get_top_weapons()

if __name__ == "__main__":
    print("Insert your nickname and tag separated by the '-' symbol and you don't need to use the hash '#' to insert the tag")
    nickname, tag = input().split('-')
    player = ValorantPlayer(nickname, tag)

    print("Rating: " + player.rating())
    print("Amount of kills: " + player.kills())
    print("Amount of assistances: " + player.assistances())
    print("Kills per round: " + player.kills_per_round())
    print("Damage per round: " + player.damage_per_round())
    print("Deaths: " + player.deaths())
    print("Top weapon: " + str(player.top_weapon()))
    print("Headshots amount: " + player.headshot_amount())
    print("Headshot percentage: " + player.headshot_percentage())
