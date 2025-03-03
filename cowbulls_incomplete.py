import random

def compare_numbers(number, user_guess):
    cows = 0 #padma_pednekar added extra lines of code
    bulls = 0

    for i in range (len(number)):
        if user_guess[i] == number[i]:
            bulls += 1
        elif user_guess[i] == number[i]:
            cows += 1
    return cows,bulls #padma_pednekar made the returns the right statement, by changing "cowbull" to "cows, bulls"

playing = True #gotta play the game
number = str(random.randint(0,9999)) #random 4 digit number
guesses = 0
print (number) #padma_pednekar added paranthesis () to the print statement

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!") #padma_pednekar changed raw_input to input
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + "guesses! The number was "+str(number)) #padma_pednekar modified the print statement and added 'guesses'
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")
