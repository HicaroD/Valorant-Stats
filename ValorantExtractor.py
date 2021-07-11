from Main import soup, page, nickname, tag, player_info

class Valorant:
    """
    Insert the tag without '#', just the characteres or numbers. 
    """
    def __init__(self, nickname, tag):
        self.nickname = nickname
        self.tag = tag 
    
    def kills(self):
        return player_info()[8]
    
    def deaths(self):
        return player_info()[10]
    
    def assistances(self):
        return player_info()[11]
    
    def kills_per_round(self):
        return player_info()[-4]
    
    def damage_per_round(self):
        return player_info()[3]

    def headshot_percentage(self):
        return player_info()[5]
    
    def clutchs(self):
        return player_info()[-3]

    def headshot_amount(self):
        return player_info()[9]

if __name__ == "__main__":
    player = Valorant(nickname, tag)
