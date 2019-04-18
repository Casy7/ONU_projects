#from main import Game
#from Steam import Steam
class Publisher(object):
	games = {}
	def __init__ (self, name, office):
		self.name = name
		self.office = office
	def addGame(self,game):
		self.games[game.name]=game

		