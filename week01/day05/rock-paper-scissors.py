# Part II - rock-paper-scissors.py


from game import Game

def get_user_menu_choice():
    print("Menu :")
    print("(g) Play a new game")
    print("(s) Show scores")
    print("(x) exit")
    return input("Enter your choice : ").lower()


def print_results(results):
    win = results.get("win", 0)
    loss = results.get("loss", 0)
    draw = results.get("draw", 0)
    print(f"You won {win} times.")
    print(f"You loss {loss} times.")
    print(f"You drew {draw} times.")
    print("Thank you for playing!")


def main():
    results = {"win": 0, "loss": 0, "draw": 0}
    while True:
        user_choice = get_user_menu_choice()
        if user_choice == "g":
            game = Game()
            result = game.play()
            if result == "won":
                results["win"] += 1
            elif result == "loss":
                results["loss"] += 1
            elif result == "draw":
                results["draw"] += 1
        elif user_choice == "s":
            print_results(results)
        elif user_choice == "x":
            print_results(results)
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()