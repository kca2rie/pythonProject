class UserInterface:
    def wait_user_answer(self):
      print(" Редактирование данных католога фильмов ".center(50, "="))
      print("Действия с фильмами")
      print("1 - добавление фильма")
      print("q - выход из программы")
      user_answer = input("Выберите вариант действия: ")
      print("=" * 50)
      return user_answer
    
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
        print("Добавление фильма: ".center(50, "="))
        for key in dict_film:
            dict_film[key] = input(f"Введите {key} фильма: ")
        print("=" * 50)
        return dict_film
