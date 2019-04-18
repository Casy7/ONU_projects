from operator import attrgetter

from Publisher import Publisher
from Steam import Steam
from Game import Game

bethesda = Publisher("Bethesda", "Maryland, USA")
eaGames = Publisher("Electronic Arts", "California, USA")

bethesda = Publisher("Bethesda", "Maryland, USA")
eaGames = Publisher("Electronic Arts", "California, USA")
skyrim = Game("Skyrim",  "Action RPG", 94.0, "11/12/2010", bethesda)
fallout = Game("Fallout 4",  "Action RPG", 84.0, "10/11/2015", bethesda)
fifa = Game("Fifa",  "Sports", 85.7, "11/09/2018", eaGames )
nba = Game("NBA",  "Sports", 75.9, "11/11/2018", eaGames )
myVideoGame = Game(name="The best game ever", genre="Chess", raiting=54.5)

bethesda.addGame(skyrim)

games = [skyrim, fifa, myVideoGame]
steam = Steam(games)
steam.addGame(nba)
steam.addGame(fallout)

bethesdaGames = steam.getGamesFromPublisher("Bethesda")
print("Bethesda games:\n")
for game in bethesdaGames:
    print(game)

print("--------------------------------------------")


print("Best games:\n")
games = [skyrim, fallout, fifa, nba, myVideoGame]
gamesByRaiting = Steam.getGamesSortedByRaiting(games)
for game in gamesByRaiting:
    print(game)

print("--------------------------------------------")

print("Fifa info:")
print(steam("Fifa"))

print("--------------------------------------------")
