#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests 
from bs4 import BeautifulSoup as bs
from threading import Thread 

                
class Valorant(object):
    def __init__(self, nick_name, riot_id):
        self.nick_name = nick_name
        self.riot_id = riot_id
        
    def web_page_stats(self):
            url = f'https://tracker.gg/valorant/profile/riot/{self.nick_name}%23{self.riot_id}/overview'.replace(' ', '+')
            source = requests.get(url = url).text
            soup = bs(source, 'lxml')
            return soup

    def get_rank(self):
        my_page = self.web_page_stats()

        rank_information = my_page.find('div', class_="valorant-highlighted-stat").find('span', class_="valorant-highlighted-stat__value").text
        return f'The rank of {self.nick_name} is {rank_information}'

    def victories(self):
        victories_page = self.web_page_stats()
        
        main_section_victories_counter = victories_page.findAll('div', class_="stat align-left expandable")[0].text.split('  ')
        return f'{self.nick_name} has won {main_section_victories_counter[2]} match(es)'
    
    def kills(self):
        kills_page = self.web_page_stats()
        number_kills = kills_page.findAll('div', class_="stat align-left expandable")[1].text.split('  ')
        
        return f'{self.nick_name} has {number_kills[2]} kill(s)'
    
    def headshot(self):
        headshot_page = self.web_page_stats()
        number_kills = headshot_page.findAll('div', class_="stat align-left expandable")[2].text.split('  ')
        
        return f'{self.nick_name} has {number_kills[2]} headshot(s)'      
    
    def deaths(self):
        """
        Returns the amount of the death
        """
        deaths_page = self.web_page_stats()
        number_deaths = deaths_page.findAll('div', class_="stat align-left expandable")[3].text.split('  ')
        
        return f'{self.nick_name} has {number_deaths[2]} death(s)'
    def assistances(self):
        assistances_page = self.web_page_stats()
        number_assistances = assistances_page.findAll('div', class_="stat align-left expandable")[4].text.split('  ')
        
        return f'{self.nick_name} has {number_assistances[2]} assistance(s)'
    def clutches(self):
        clutches_pages = self.web_page_stats()
        number_clutches = clutches_pages.findAll('div', class_="stat align-left expandable")[7].text.split('  ') 
        
        return f'{self.nick_name} has won {number_clutches[2]} clutch(es)'
    
    def top_weapons(self):
        weapons_page = self.web_page_stats()
        
        print(f'\n{self.nick_name}, your top weapons:')
        
        for index in range(3):
                weapon_name = weapons_page.findAll('div', class_="weapon__name")[index].text
                top_weapons_kills = weapons_page.findAll('div', class_='weapon__main-stat')[index].text
                
                print(f'\t \t{weapon_name} ---> {top_weapons_kills}')
        print("\n")

    def accuracy(self):
        accuracy_content = self.web_page_stats()
        print(f"{self.nick_name}, your accuracy informations:")

        accuracy = accuracy_content.find('table', class_='accuracy__stats').find('tbody').text.split(' ')
        
        head_accuracy = accuracy[:4]
        body_accuracy = accuracy[4:8]
        legs_accuracy = accuracy[8:]

        print(f"\t \t{head_accuracy[0]} --> {head_accuracy[1]} --> {head_accuracy[2]} {head_accuracy[3]}\n\t \t{body_accuracy[0]} --> {body_accuracy[1]} --> {body_accuracy[2]} {body_accuracy[3]}\n\t \t{legs_accuracy[0]} --> {legs_accuracy[1]} --> {legs_accuracy[2]} {legs_accuracy[3]}")
        

#Insert the nickname of the player and your Riot ID to get your stats, such as rank, kills, victories and headshot


if __name__ == '__main__':
    nick_name = input("Type your username: ")
    riot_id = input("Type your Riot ID: ")    
    print("\n \n")
    
    player_1 = Valorant(nick_name, riot_id)


    try:
        print(player_1.get_rank()) #Get your rank information
        print(player_1.victories()) # Do you want to see how many victories you have?
        print(player_1.kills()) # Wanna see how many kill you get?
        print(player_1.headshot()) # What about headshot? 
        print(player_1.deaths()) # How many times you died? 
        print(player_1.assistances()) # Do you help your team? Check it out 
        print(player_1.clutches()) # Are you really strong at this game? Check how many clutches you achieved
        player_1.top_weapons() # See your top weapons based on your kills
        player_1.accuracy()
    except AttributeError as e:
        print("Make sure that your account is not private. Otherwise, we can't acess nothing at all. Also make sure that you typed the nickname and Riot ID correctly\n\nPlease read the repository to solve/report possible problems: https://github.com/HicaroD/Valorant-Stats\n")