import random
number= random.randint(1,10)
Value= int(input("Enter a number between 1 to 10: "))
if number==Value:
    print("You won!")
else:
    print("You lose!, better luck next time.")    
    print("The actual number was", number)