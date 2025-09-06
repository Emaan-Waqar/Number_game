import random
print("Rock, paper,Scissors!!!")
print("Options: rock, paper, scissors")
options= ["rock", "paper", "scissors"]
user= input("\nEnter your choice: ")    
user=user.lower()
comp= random.choice(options)
print("\nYou chose", user)
print("Computer chose", comp)

if user==comp:
    print("\nTie!!")
elif user == "rock" and comp == "scissors":
    print("\nYou Won!!") 
elif user == "paper" and comp == "rock":  
    print("\nYou Won!!")  
elif user == "scissors" and comp == "paper":  
    print("\nYou won!!")  
else: 
    print("\nYou lost. :(")    