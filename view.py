def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output
        return wrap
    
    return wrapper


class UserInterface:
    @add_title('Ввод пользовательских данных')
    def wait_user_answer(self):
        print("Действия с фильмами:")
        print("1 - добавление фильма"
            "2 - каталог фильмов"
            "q - выход из программы")
      user_answer = input("Выберите вариант действия: ")
      return user_answer
    
    @add_title('Добавление фильма:')
    def add_user_film(self):
        dict_film = {
            "название" : None,
            "жанр": None,
            "режиссёр": None,
            "год выпуска": None,
            "длительность": None,
            "студия": None,
            "актёры": None
      } 
        for key in dict_film:
            dict_film[key] = input(f"Введите {key} фильма: ")
        return dict_film
    
    @add_title('Каталог фильмов:')
    def show_all_films(self, films):
        for ind, film in enumerate(films, start=1):
            print(f"{ind}. {films}")
