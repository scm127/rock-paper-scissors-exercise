import random
import os
from dotenv import load_dotenv

load_dotenv()
PLAYER_NAME=os.getenv("PLAYER_NAME", default="Player One")

print("----------------")
print("Welcome ", PLAYER_NAME, " to my Rock-Paper-Scissors game...")
print("----------------")

user_input= input("Please choose either 'rock', 'paper', or 'scissors' :")
print("----------------")

user_input.lower()
rps= ["rock","paper","scissors"]
if user_input not in rps:
    print("Please enter a valid option and try again")
    exit()

print("You chose: ", user_input)


computer_choice= random.choice(rps)
print("The computer chose: " , computer_choice)



if computer_choice==user_input:print("it's a tie")
elif user_input == "paper" and computer_choice == "rock": print("You win! Congrats")
elif user_input == "paper" and computer_choice == "scissors": print("Oh! The computer won, that's ok!")
elif user_input == "rock" and computer_choice == "paper": print("Oh! The computer won, that's ok!")
elif user_input == "rock" and computer_choice == "scissors": print("You win! Congrats")
elif user_input == "scissors" and computer_choice == "paper": print("You win! Congrats")
elif user_input == "scissors" and computer_choice == "rock": print("Oh! The computer won, that's ok!")

exit()



