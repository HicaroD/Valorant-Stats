from distutils.core import setup

setup(
    name="ValorantExtractor",
    packages=["ValorantExtractor"], 
    version='0.1', 
    license="MIT", 
    description="Obtain your valorant stats withou the Riot API!",
    author="Hícaro Dânrlley", 
    author_email="hdanrlley1@gmail.com", 
    requires=[
        "beautifulsoup4",
        "requests"
    ],
    url="https://github.com/HicaroD/Valorant-Stats",
    keywords=["Valorant", "Stats", "Without API", "Informations"],

)