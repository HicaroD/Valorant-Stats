from ValorantExtractor import Valorant


player = Valorant("TXC H1CARO", "6761")

print(player.rating())

print(player.kills())

print(player.assistances())

print(player.kills_per_round())

print(player.damage_per_round())

print(player.deaths())

print(player.top_weapon()) # Dictionary 

print(player.headshot_amount())

print(player.headshot_percentage())