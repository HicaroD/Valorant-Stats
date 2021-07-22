# Valorant Stats by H1CARO

![](Images/1072679.jpg)


## Goal
Learn more about Web Scraping with BeautifulSoup and Requests libraries. I'm using both libraries to extract informations from a website called tracker.gg/valorant

That's just for educational purposes and nothing more! 

## Libraries 
* BeautifulSoup - Python library for pulling data out of HTML and XML files
* Requests -  a simple, yet elegant HTTP library that allows you to send HTTP/1.1 requests extremely easily. 


## Read this first
To acess your informations through this program, your Riot Account has to be public. How do you know this?

### 1. Go to https://tracker.gg/valorant
On https://tracker.gg/valorant, Type your nickname and Riot ID.

![](Images/private_acc.png)

If that shows up, your account is private. Now, select that checkbox "I acknowledge signing in makes my profile public to all users" and sign in with your Riot account. After that, everyone can acess your stats about the game. Don't worry, this won't expose your privacy, it will just set your account to be public in relation to your game information like kill count, headshots, rank and so on.


## Instalation of libraries

#### 1. Installing pip

Pip is the package installer for Python. On Linux, you can install through the terminal.

```
sudo apt install python3-pip

```

#### 2. Cloning my repository

```
git clone https://github.com/HicaroD/Valorant-Stats.git

```

#### 3. Installing the packages

First, go to the Valorant-Stats folder using ``` cd Valorant-Stats ``` and after that you can install the packages using ``` pip3 install -r requirements.txt```

NOTE: pip3 is the newest version of Pip at the momento, make sure you updated it.  

## Examples
``` python3

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
```
