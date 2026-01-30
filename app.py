"""
Docstring for game_logic.app
"""
from game_logic import game
from menu import display_menu
from game import two_players

def main():
    """
    Main function to run the tic tac toe game
    """
    while True:
        choice = display_menu()
        if choice == 1:
            print("In progress")
        elif choice == 2:
            two_players()
        elif choice == 3:
            print("Exiting the game. Goodbye!")

if __name__ == "__main__":
    two_players()
