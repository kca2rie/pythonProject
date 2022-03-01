from view import UserInterface

class Controller:
    def __init__(init):
        self.film_model = None
        self.user_interface = UserInterface()
        
    def run(self):
        answer = None
        while answer != 'q':
            answer = self.user_interface.wait_user_answer()
