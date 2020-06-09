## this is a simple program to have the user guess a random number
## for simplicity the random number will be bewtween 0 and 1000 , the user will have a massege to show if the inputed number is lower or higher than the random number
import random
rand = random.randint(0,1000) # assigning the the random number to the variable rand
user_input = int(input(" Hello , try to guess a number between 0 and 1000 : "))

while user_input != rand :
    if user_input < rand : # in case if the input is lower
        user_input = int(input("Your number is lower than the random number , try again : ")) # another try for the user in the new number will be assigned to user_input
    if user_input > rand :  # in case if the input is higer
        user_input = int(input("Your number is higer than the random number , try again : ")) # another try for the user in the new number will be assigned to user_input

print(" Yes you finally guessed it right ! \n the number is : " , rand)