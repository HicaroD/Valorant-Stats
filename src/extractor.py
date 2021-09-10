from bs4 import BeautifulSoup as bs4
import requests

class WebExtractor:
    def __init__(self, nickname, tag):
        self.nickname = nickname
        self.tag = tag

    def get_webpage(self):
        return requests.get(f'https://tracker.gg/valorant/profile/riot/{self.nickname}%23{self.tag}/overview').text

    def parse_webpage(self):
       try:
           page = self.get_webpage()
           soup = bs4(page, 'lxml')
           return soup

       except Exception as e:
          print(f"Error: {e}. Make sure your account is public. Read this: https://github.com/HicaroD/Valorant-Stats\n")

class PlayerInfoExtractor:
    def __init__(self, nickname, tag):
        self.nickname = nickname
        self.tag = tag
        self.page = WebExtractor(self.nickname, self.tag).parse_webpage()

    def get_individual_performance(self):
        """
        Obtains informations about the competitive overview, like kills, assistances, amount of
        headshot and return it as a list of values
        """

        divs = self.page.find_all("span", {"class":"value"})
        values = [div.text for div in divs]
        return values

    def get_player_rating(self):
        return self.page.find("span", {"class": "valorant-highlighted-stat__value"}).text

    def get_top_weapons(self):
        """
        Returns as a dictionary. The list is gonna store the name of the weapon, accuracy (headshot, bodyshot and leg shots)
        and the number of kills with the weapon
        """
        try:
            top_weapon = self.page.find("div", {"class": "weapon"}).text.split(" ")

            top_weapon_informations = {"Weapon": top_weapon[1], "Headshots": top_weapon[-5],"Bodyshot": top_weapon[-4],
                                       "Leg_shot":top_weapon[-3], "Kills": top_weapon[-1]}

            return top_weapon_informations

        except Exception as e:
            print(f"Error: {e}. Make sure if it's the correct nickname and tag. Otherwise, it might be about your account visibility, check if it's public.")
            print("Otherwise, it might be about your account visibility, check if it's public. Read : https://github.com/HicaroD/Valorant-Stats\n")

