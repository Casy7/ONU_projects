class Game(object):
	def __init__ (self, name, genre, raiting, date = None,company = None):
		self.name = name
		self.genre = genre
		self.raiting = raiting
		self.date = date
		self.company = company
	def __str__(self):
		to_return=""
		if(self.name!=None):
			to_return=self.name+"\n"
			if self.date!=None:
				to_return=to_return+"Release date:	"+str(self.date)+"\n"
			to_return=to_return+"Raiting:	"+str(self.raiting)+"\n"+"Genre:	"+self.genre+"\n"
			if self.company!=None:
				to_return=to_return+"Release date:	"+self.company.name+"from"+self.company.office+"\n"
		return to_return	