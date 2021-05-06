#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests 
from bs4 import BeautifulSoup as bs
                
class Valorant(object):
    def __init__(self, nick_name, riot_id):
        self.nick_name = nick_name
        self.riot_id = riot_id


    def get_rank(self):
        source = requests.get(url = f'https://tracker.gg/valorant/profile/riot/{self.nick_name}%23{self.riot_id}/overview'.replace(' ', '+')).text
        soup = bs(source, 'lxml')

        rank_information = soup.find('div', class_="valorant-highlighted-stat").find('span', class_="valorant-highlighted-stat__value").text
        return f'Your rank is {rank_information}'

    def victories(self):
        source = requests.get(url=f'https://tracker.gg/valorant/profile/riot/{self.nick_name}%23{self.riot_id}/overview'.replace(' ', '+')).text
        soup = bs(source, 'lxml')
        
        main_section_victories_counter = soup.findAll('div', class_="stat align-left expandable")[0].text.split('  ')
        return f'You have won {main_section_victories_counter[2]} match(es)'
    
        # for i in range(10):
        #     main_section_victories_counter = soup.findAll('div', class_="stat align-left expandable")[i].text.split('  ')
        #     print(main_section_victories_counter)
    def kills_counter(self):
        source = requests.get(url=f'https://tracker.gg/valorant/profile/riot/{self.nick_name}%23{self.riot_id}/overview'.replace(' ', '+')).text
        soup = bs(source, 'lxml')
        number_kills = soup.findAll('div', class_="stat align-left expandable")[1].text.split('  ')
        
        return f'You have {number_kills[2]} kill(s)'
    
    def headshot_counter(self):
        source = requests.get(url=f'https://tracker.gg/valorant/profile/riot/{self.nick_name}%23{self.riot_id}/overview'.replace(' ', '+')).text
        soup = bs(source, 'lxml')
        number_kills = soup.findAll('div', class_="stat align-left expandable")[2].text.split('  ')
        
        return f'You have {number_kills[2]} headshot(s)'
        

#Insert the nickname of the player and your Riot ID to get your stats, such as rank, kills, victories and headshot
player_1 = Valorant('TXC BOLADONA', '2050')
print(player_1.get_rank())
print(player_1.victories())
print(player_1.kills_counter())
print(player_1.headshot_counter())
