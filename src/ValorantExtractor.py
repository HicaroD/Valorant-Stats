from bs4 import BeautifulSoup as bs4
import requests
from requests.api import head, request 

class ValorantPlayer:
    def __init__(self, nickname, tag):
        self.nickname = nickname
        self.tag = tag
        self.page = self._get_webpage()
        self.player_info = self._player_info()
    
    def kills(self): 
        return self.player_info[8]
    
    def deaths(self):
        return self.player_info[10]   

    def assistances(self):
        return self.player_info[11]
    
    def kills_per_round(self):
        return self.player_info[-4]
    
    def damage_per_round(self):
        return self.player_info[3]

    def headshot_percentage(self):
        return self.player_info[5]
    
    def clutchs(self):
        return self.player_info[-3]

    def headshot_amount(self):
        return self.player_info[9]

    def rating(self):
        return self.page.find("span", {"class": "valorant-highlighted-stat__value"}).text
    
    def top_weapon(self):
        """
        Returns as a dictionary. The list is gonna store the name of the weapon, accuracy (headshot, bodyshot and leg shots) and the number of kills
        with the weapon
        """
        top_weapon = self.page.find("div", {"class": "weapon"}).text.split(" ")
        
        top_weapon_informations = {"Weapon": top_weapon[1], "Headshots": top_weapon[-5],
                                   "Bodyshot": top_weapon[-4], "Leg_shot":top_weapon[-3], "Kills": top_weapon[-1]}

        return top_weapon_informations
    
    
    def _get_webpage(self): 
        page = requests.get(f'https://tracker.gg/valorant/profile/riot/{self.nickname}%23{self.tag}/overview').text
        soup = bs4(page, 'lxml')    

        return soup

    def _player_info(self):
        """
        Obtains informations about the competitive overview, like kills, assistances, amount of
        headshot and return it as a list of values  
        """

        divs = self.page.find_all("span", {"class":"value"})
        values = [div.text for div in divs]
        
        return values

if __name__ == "__main__":
    player = ValorantPlayer("TXC H1CARO", "6761")
    print(player.rating())
    print(player.kills())
    print(player.assistances())
    print(player.kills_per_round())
    print(player.damage_per_round())
    print(player.deaths())
    print(player.top_weapon())
    print(player.headshot_amount())
    print(player.headshot_percentage())




    