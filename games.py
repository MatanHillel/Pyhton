##############################################
##########7Boom
# number = 1
# while number < 100:
#     if number % 7 == 0 or '7' in str(number):
#         print("Boom")
#     else:
#         print(number)
#     number+= 1
# ##############################################
#
#
# ##############################################
############rock pepar scissors
# import random
#
# player_name = input("Hello sir! what is your name? ")
# Options_list = ['stone', 'paper', 'scissors']
# PC_hand = random.choice(Options_list)
# result_player = 0
# result_PC = 0
#
#
# # Rules:
# def game_rules(player_hand, PC_hand):
#     if player_hand == 'stone' and PC_hand == 'scissors':
#         return 'player wins!'
#     if player_hand == 'stone' and PC_hand == 'paper':
#         return 'PC wins!'
#     if player_hand == 'scissors' and PC_hand == 'paper':
#         return 'player wins!'
#     if player_hand == 'scissors' and PC_hand == 'stone':
#         return 'PC wins!'
#     if player_hand == 'paper' and PC_hand == 'scissors':
#         return 'PC wins!'
#     if player_hand == 'paper' and PC_hand == 'stone':
#         return 'player wins!'
#     else:
#         return 'TIE!'
#
#
# rounds_to_play = 5  # Play X rounds untill reaching the number of rounds listed here or untill getting 3 points.
#
# while result_player < rounds_to_play and result_PC < rounds_to_play:
#     player_hand = input("Choose an option- ").strip().lower()
#     PC_hand = random.choice(Options_list)
#
#     result = game_rules(player_hand, PC_hand)
#     print(f"Player chose {player_hand}, PC chose {PC_hand}. Result: {result}")
#
#     # +1 for the winner
#     if result == 'player wins!':
#         result_player += 1
#     elif result == "PC wins!":
#         result_PC += 1
#     if result_player == 3 or result_PC == 3:
#         break
#
# # result of the game
# if result_player > result_PC:
#     print(f"{player_name} wins!")
# elif result_player < result_PC:
#     print("PC wins!")
# else:
#     print("It's tie!")

##############################################

############ rock paper siccers CHATGPT
#import random

#def get_user_choice():
#    while True:
#        user_choice = input("Choose Rock, Paper, or Scissors: ").strip().lower()
#        if user_choice in ["rock", "paper", "scissors"]:
#            return user_choice
#        else:
#            print("Invalid choice. Please enter Rock, Paper, or Scissors.")

#def get_computer_choice():
#    choices = ["rock", "paper", "scissors"]
#    return random.choice(choices)

#def determine_winner(user_choice, computer_choice):
#    if user_choice == computer_choice:
#        return "It's a tie!"
#    elif (
#        (user_choice == "rock" and computer_choice == "scissors")
#        or (user_choice == "paper" and computer_choice == "rock")
#        or (user_choice == "scissors" and computer_choice == "paper")
#    ):
#        return "You win!"
#    else:
#        return "Computer wins!"

#def main():
#    print("Welcome to Rock, Paper, Scissors!")
#    while True:
#        user_choice = get_user_choice()
#        computer_choice = get_computer_choice()
#        print(f"You chose {user_choice}. Computer chose {computer_choice}")
#        result = determine_winner(user_choice, computer_choice)
#        print(result)

#        play_again = input("Play again? (yes/no): ").strip().lower()
#        if play_again != "yes":
#            break

#if __name__ == "__main__":
#    main()

##############################################

#wordle
#6 attempts
import random

def target_word():
    list_t_word = ['split','stick']
    choose = random.choice(list_t_word)
    tar_word = list(choose)
    return tar_word

def palyer_choice():
    choice = input("chose word:")
    list_choice = list(choice)
    return list_choice

def the_game(listi, list_target):
    result = []
    for i, char in enumerate(listi):
        if char == list_target[i]:
            result.append(f"\033[0;32m{char}")
        elif char in list_target:
            result.append(f"\033[1;33m{char}")
        else:
            result.append(f"\033[0;37m{char}")
    return ''.join(result)

n=0
target = target_word()
while n<=6:
    choosing = palyer_choice()
    n+=1
    print(the_game(choosing,target))
#enumerate(my_list) returns an iterator that yields pairs of (index, element)
# enumerate is a built-in Python function that allows you to iterate over an iterable
# (such as a list, tuple, or string) while keeping track of both the elements
# and their corresponding indices. It returns pairs of (index, element)
# for each item in the iterable. Here's how it works#print("\033[0;32m This text is Bright Green")
###########################################
# my_list = ['apple', 'banana', 'cherry']
#
# for index, element in enumerate(my_list):
#     print(f'Index: {index}, Element: {element}')
#
# print:
# Index: 0, Element: apple
# Index: 1, Element: banana
# Index: 2, Element: cherry