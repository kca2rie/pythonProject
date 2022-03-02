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
        
class Film Model:
    def __init__(self):
        self.films = {}
        
    def add_film(self, dict_film):
        film = Film(*dict_film.values())
        self.films[films.title] = film
