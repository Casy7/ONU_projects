class Movie():
	def __init__(self, name, duration, releaseDate, rating):
		self.name = name
		self.duration = duration
		self.releaseDate = releaseDate
		self.rating = rating
	def show_info(self, movie):
		print("Фильм \"",movie.name,"\"","\n","Продолжительность: ",movie.duration,"\n","Рейтинг: ",movie.rating,"\n",sep="")

ready_Player_One = Movie("Первому игроку приготовиться","2:20","2018",7.417)
ready_Player_One.show_info(ready_Player_One)
harry_Potter = Movie("Гарри Поттер и философский камень","2:32","2001",8.4)
lord_of_the_rings = Movie("Властелин колец: Братство кольца","2:58","2001",8.6)
pirates = Movie("Пираты Карибского моря 1","2:58","2003",8.3)
terminator = Movie(" Терминатор","1:47","1984",8.3)

movie_list = [ready_Player_One, harry_Potter, lord_of_the_rings, pirates, terminator]

class Critic():
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def get_best_movie(self, movie_list):
		best_rating = 0
		for current_movie in movie_list:
			if current_movie.rating>best_rating:
				best_rating_film = current_movie
				best_rating = current_movie.rating
		return best_rating_film.name
	@staticmethod
	def get_movies_for_year(year):
		at_this_year = []
		for current_movie in movie_list:
			if current_movie.releaseDate==year:
				at_this_year.append(current_movie.name)
		return at_this_year
Casy = Critic("Casy",16)

input_year = "2001"

print("В",input_year, "году: ",', '.join(Casy.get_movies_for_year(input_year)))
print("Лучший фильм - это",Casy.get_best_movie(movie_list))