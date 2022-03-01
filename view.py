class UserInterface:
    def wait_user_answer(self):
      print(" Редактирование данных католога фильмов ".center(50, "="))
      print("Действия с фильмами")
      print("q - выход из программы")
      user_answer = input("Выберите вариант действия: ")
      print("=" * 50)
      return user_answer
