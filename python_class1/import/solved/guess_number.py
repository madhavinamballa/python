##Number Guess game 
import random
user_guess=int(input("Eneter any integer between 1 and 99: "))
computer_choice = random.randint(1, 99)
while computer_choice != "guess":
    print
    if user_guess < computer_choice:
        print ("guess is low!")
        user_guess = int(input("Enter an integer from 1 to 99: "))
    elif user_guess > computer_choice:
        print ("guess is high!Try again")
        user_guess = int(input("Enter an integer from 1 to 99: "))
    else:
        print ("you guessed it!")
        break
    print

