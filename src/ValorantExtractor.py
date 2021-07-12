from bs4 import BeautifulSoup as bs4
import requests
from requests.api import head, request 

def player_info(nickname, tag):
    """
    Obtains informations about the competitive overview, like kills, assistances, amount of
    headshot and return it as a list of values  
    """
    soup = get_webpage(nickname, tag)

    divs = soup.find_all("span", {"class":"value"})
    
    values = []
    
    for i in range(len(divs)):
        values.append(divs[i].text)
        
    return values

def get_webpage(nickname, tag):
    page = requests.get(f'https://tracker.gg/valorant/profile/riot/{nickname}%23{tag}/overview').text

    soup = bs4(page, 'lxml')    
    return soup


class Valorant:
    """
    Insert the tag without '#', just the characteres or numbers. 
    """
    def __init__(self, nickname, tag):
        self.nickname = nickname
        self.tag = tag
    
    def kills(self):
        kills = player_info(self.nickname, self.tag)[8]
        return kills
    
    def deaths(self):
        deaths = player_info(self.nickname, self.tag)[10]
        return deaths   

    def assistances(self):
        assistances = player_info(self.nickname, self.tag)[11]
        return assistances
    
    def kills_per_round(self):
        kills_per_round = player_info(self.nickname, self.tag)[-4]
        return kills_per_round
    
    def damage_per_round(self):
        damage_per_round = player_info(self.nickname, self.tag)[3]
        return damage_per_round

    def headshot_percentage(self):
        headshot_percentage = player_info(self.nickname, self.tag)[5]
        return headshot_percentage
    
    def clutchs(self):
        clutchs = player_info(self.nickname, self.tag)[-3]
        return clutchs

    def headshot_amount(self):
        headshot_amount = player_info(self.nickname, self.tag)[9]
        return headshot_amount

    def rating(self):
        page = get_webpage(self.nickname, self.tag)
        rating = page.find("span", {"class": "valorant-highlighted-stat__value"}).text
        return rating
    
    def top_weapon(self):
        """
        Returns as a dictionary. The list is gonna store the name of the weapon, accuracy (headshot, bodyshot and leg shots) and the number of kills
        with the weapon
        """
        page = get_webpage(self.nickname, self.tag)
        
        #List of values
        top_weapon = page.find("div", {"class": "weapon"}).text.split(" ")
        
        top_weapon_informations = {"Weapon": top_weapon[1], "Headshots": top_weapon[-5],
        "Bodyshot": top_weapon[-4], "Leg shot":top_weapon[-3], "Kills": top_weapon[-1]}

        return top_weapon_informations

if __name__ == "__main__":
    # nickname, tag = input().split("-")
    player = Valorant("TXC H1CARO", "6761")
    print(player.rating())