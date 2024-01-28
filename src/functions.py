import random
from chocies import Choices

def welcome(): 
    print("Welcome to the Rock Paper Scissors GAME! Let's PLAY!!!")
    print("--------------------------------------------------")
    
def get_choice_input():
    while(True):
        try:
            choice = int(input("Press 1: Scissors, Press 2: Paper, Press 3: Rock\n"))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid input! Please choose a correct alternative!")
        except:
            print("Invalid input! Please choose a correct alternative!")
        
def generate_computer_choice(): 
    return random.randrange(1, 3)

def present_chooser_and_choice(chooser: str, choice: str):
    match Choices(choice):
        case Choices.SCISSORS:
            print(f"{chooser}: {Choices.SCISSORS.name}")
        case Choices.PAPER:
            print(f"{chooser}: {Choices.PAPER.name}")
        case Choices.ROCK:
            print(f"{chooser}: {Choices.ROCK.name}")

def check_winner(user_choice, comp_choice):
    outcomes = {
        (1, 2): "You won!",
        (1, 3): "You lost!",
        (2, 1): "You lost!",
        (2, 3): "You won!",
        (3, 1): "You won!",
        (3, 2): "You lost!",
    }

    outcome = outcomes.get((user_choice, comp_choice), "Tie!")
    return outcome
    
def play_again():
    choice = input("Would you like to play again? Type Y(es) or any other letter to quit!\n") 
    return True if choice.lower() == "y" or choice.lower() == "yes" else False