from extractor import WebExtractor, PlayerInfoExtractor
from bs4 import BeautifulSoup as bs4
import requests

class ValorantPlayer:
    def __init__(self, nickname, tag):
        self.nickname = nickname
        self.tag = tag
        self.player_info = PlayerInfoExtractor(self.nickname, self.tag)

    def individual_perfomance(self, index):
        return self.player_info.get_individual_performance()[index]

    def kills(self):
        return self.individual_perfomance(8)

    def deaths(self):
        return self.individual_perfomance(10)

    def assistances(self):
        return self.individual_perfomance(11)

    def kills_per_round(self):
        return self.individual_perfomance(-4)

    def damage_per_round(self):
        return self.individual_perfomance(3)

    def headshot_percentage(self):
        return self.individual_perfomance(5)

    def clutchs(self):
        return self.individual_perfomance(-3)

    def headshot_amount(self):
        return self.individual_perfomance(9)

    def rating(self):
        return self.player_info.get_player_rating()

    def top_weapon(self):
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
