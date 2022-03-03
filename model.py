import pickle
import os.path

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
        self.db_name = "db.txt"
        self.films = self.load_data()
        
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
        
    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, "rb") as f:
                return pickle.load(f)
        else:
            return dict()
        
    def save_data(self):
        with open(self.db_name, "wb") as f:
            pickle.dump(self.films, f)
