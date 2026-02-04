"""
Docstring for game_logic.app
"""
from menu import display_menu
from game import play_game

def main():
    """
    Main function to run the tic tac toe game
    """
    while True:
        choice = display_menu()
        if choice == 1:
            play_game(1)
        elif choice == 2:
            play_game(2)
        elif choice == 3:
            print("Exiting the game. Goodbye!")
            break

if __name__ == "__main__":
    main()
