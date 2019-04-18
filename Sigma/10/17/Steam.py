from Publisher import Publisher
#from main import Game

class Steam(object):
	global ready_dict
	ready_dict={}
	def __init__ (self, games = None,ready_dict={}):
		self.games = games
		self.ready_dict = ready_dict
	def
	def addGame(self,game):
		for some_game in list(self.games):
			if some_game.company!=None:
				self.ready_dict[some_game.company]=some_game
	#def addGame(self,game):
	#	self.dict_of_games[game.name] = game

	def getGamesFromPublisher (self, publisher_name):
		return_games=[]
		for some_game in self.ready_dict:
			if some_game == publisher_name:
				return_games.append(some_game)
		return(return_games)
			
			