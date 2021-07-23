from bs4 import BeautifulSoup as bs4
import requests
from requests.api import head, request 

class ValorantPlayer:
    def __init__(self, nickname, tag):
        self.nickname = nickname
        self.tag = tag
        self.page = self._get_webpage()
        self.player_info = self._player_info()
        self.top_weapon_page = self._top_weapon_info()
    
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
        return self.top_weapon_page
    
    def _top_weapon_info(self):
        """
        Returns as a dictionary. The list is gonna store the name of the weapon, accuracy (headshot, bodyshot and leg shots) and the number of kills
        with the weapon
        """ 
        try: 
            top_weapon = self.page.find("div", {"class": "weapon"}).text.split(" ")
        
            top_weapon_informations = {"Weapon": top_weapon[1], "Headshots": top_weapon[-5],"Bodyshot": top_weapon[-4], 
                                       "Leg_shot":top_weapon[-3], "Kills": top_weapon[-1]}

            return top_weapon_informations

        except Exception as e: 
            print(f"Error: {e}. Make sure if it's the correct nickname and tag. Otherwise, it might be about your account visibility, check if it's public. Read this: https://github.com/HicaroD/Valorant-Stats\n")

    def _get_webpage(self):
        try: 
            page = requests.get(f'https://tracker.gg/valorant/profile/riot/{self.nickname}%23{self.tag}/overview').text
            soup = bs4(page, 'lxml')    

            return soup

        except Exception as e: 
            print(f"Error: {e}. Make sure you had set your account to public. Read this: https://github.com/HicaroD/Valorant-Stats\n")

    def _player_info(self):
        """
        Obtains informations about the competitive overview, like kills, assistances, amount of
        headshot and return it as a list of values  
        """

        divs = self.page.find_all("span", {"class":"value"})
        values = [div.text for div in divs]
        
        return values

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




    