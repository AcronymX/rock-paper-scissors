from functions import welcome
from functions import get_choice_input
from functions import generate_computer_choice
from functions import present_chooser_and_choice
from functions import check_winner
from functions import play_again

game_continue = True
welcome()

while game_continue:
    
    user_choice = get_choice_input()
    comp_choice = generate_computer_choice()

    print("--------------------------------------------------")
    present_chooser_and_choice("You", user_choice)
    present_chooser_and_choice("Computer", comp_choice)
    print("--------------------------------------------------")

    outcome = check_winner(user_choice, comp_choice)
    print(outcome)
    
    if outcome != 'Tie!':
        game_continue = play_again()

