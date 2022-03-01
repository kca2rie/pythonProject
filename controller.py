from view import UserInterface

class Controller:
    def __init__(init):
        self.film_model = None
        self.user_interface = UserInterface()
        
    def run(self):
        answer = None
        while answer != 'q':
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)
            
    def check_user_answer(self, answer):
        if answer == "1":
            film = self.user_interface.add_user_film()
