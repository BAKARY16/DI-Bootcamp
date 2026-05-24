# Partie I - game.py
import random

class Game:
    def get_user_item(self):
        while True:
            user_item = input("Select rock: (r) or paper: (p) or scissors: (s) : ").lower()
            if user_item in ["r", "p", "s"]:
                return user_item
            print("Invalid entry. Please try again.")

    def get_computer_item(self):
        computer_item = ["r", "p", "s"]
        return random.choice(computer_item)
    
    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (user_item == "r" and computer_item == "s") or \
             (user_item == "p" and computer_item == "r") or \
                (user_item == "s" and computer_item == "p"):
            return "won"
        else:
            return "loss"
        
    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        if result == "won":
            result_text = "won"
        elif result == "loss":
            result_text = "loss"
        else:
            result_text = "draw"

        print(f"You chose {user_item}. The computer chose {computer_item}. result {result_text}.")
        return result

