# Valorant information extractor 
from bs4 import BeautifulSoup as bs4_extractor
import requests
from requests.api import request

# Obter informações in-game do jogador através do tracker.gg
def player_info():
    # Get the HTML TAG 
    divs = soup.find_all("span", {"class":"value"})
    info_size = len(divs)
    values = []
    #Extract informations from the tag and store it
    for i in range(info_size):
        values.append(divs[i].text)
        
    return values

def top_agent_info():
    top_agent_container = soup.find("div", {"class":"top-agents__table-container"}).find("table").find_all("tr")
    top_agent_size = len(top_agent_container)
    top_agent_info = []
    for i in range(top_agent_size):
        top_agent_info.append(top_agent_container[i].text)
    print(top_agent_info)

nickname, tag = input("Digite nickname e tag separados por um traço. Dessa forma: nickname-tag: \n").split('-')

# Página HTML do tracker.gg
page = requests.get(f'https://tracker.gg/valorant/profile/riot/{nickname}%23{tag}/overview').text

# Extrator das informações da página HTML e armazenando a página em soup 
soup = bs4_extractor(page, 'lxml')
top_agent_info()