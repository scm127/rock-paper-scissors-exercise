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

rps= ["rock","paper","scissors"]
RPS= ["Rock", "Paper", "Scissors"]
if user_input not in rps and RPS:
    print("Please enter a valid option and try again")
    exit()

print("You chose: ", user_input)


computer_choice= random.choice(rps)
print("The computer chose: " , computer_choice)
print("----------------")

# I added the last 9 lines of the code to allow for an uppercase first letter becasue I could not get the lower() fuction to work properly. 

if computer_choice==user_input:print("it's a tie")
elif user_input == "paper" and computer_choice == "rock": print("You win! Congrats")
elif user_input == "paper" and computer_choice == "scissors": print("Oh! The computer won, that's ok!")
elif user_input == "rock" and computer_choice == "paper": print("Oh! The computer won, that's ok!")
elif user_input == "rock" and computer_choice == "scissors": print("You win! Congrats")
elif user_input == "scissors" and computer_choice == "paper": print("You win! Congrats")
elif user_input == "scissors" and computer_choice == "rock": print("Oh! The computer won, that's ok!")

if computer_choice==user_input:print("it's a tie")
elif user_input == "Paper" and computer_choice == "rock": print("You win! Congrats")
elif user_input == "Paper" and computer_choice == "scissors": print("Oh! The computer won, that's ok!")
elif user_input == "Rock" and computer_choice == "paper": print("Oh! The computer won, that's ok!")
elif user_input == "Rock" and computer_choice == "scissors": print("You win! Congrats")
elif user_input == "Scissors" and computer_choice == "paper": print("You win! Congrats")
elif user_input == "Scissors" and computer_choice == "rock": print("Oh! The computer won, that's ok!")
elif user_input == "Paper" and computer_choice == "paper": print("it's a tie")
elif user_input == "Scissors" and computer_choice == "scissors": print("it's a tie")
elif user_input == "Rock" and computer_choice == "rock": print("it's a tie")
exit()



