class Film:
    def __init__(self, title, genre, director, year, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors
        
    def __str__(self):
        return f"{self.title} ({self.genre})"
        
class FilmModel:
    def __init__(self):
        self.films = {}
        
    def add_film(self, dict_film):
        film = Film(*dict_film.values())
        self.films[films.title] = film
        
        
    def get_all_films(self):
        return self.films.values()
    
    def get_single_film(self, user_title):
        film - self.films[user_title]
        dict_film = {
            'название': film.title,
            'жанр': film.genre,
            'режиссер': film.director,
            'годы выпуска': film.year,
            'длительность': film.duration,
            'студия': film.studio,
            'актёры': film.actors
        }
        return dict_films
    
    def remove_film(self, user_title):
        returm self.films.pop(user_title)
