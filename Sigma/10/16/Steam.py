from operator import attrgetter
from Publisher import Publisher
#from main import Game

class Steam(object):
	def __init__ (self, games = None, dict_games = {}):
		#self.games = games
		dict_games={}
		for game in games:
			dict_games[game.name] = game
		self.dict_games = dict_games
		self.games = games
	
	def addGame(self, game):
		self.games.append(game)
		#self.games.game.name = game
	#def addGame(self,game):
	#	self.dict_of_games[game.name] = game

	def getGamesFromPublisher (self, publisher_name):
		return_games=[]
		for some_game in self.games:
			if some_game.company!=None:
				if some_game.company.name == publisher_name:
					return_games.append(some_game)
		return(return_games)
	@staticmethod
	def getGamesSortedByRaiting(games):
		return(sorted(games, key = attrgetter('raiting'),reverse = True))

	def __call__(self, name):
		return self.dict_games.get(name)
			