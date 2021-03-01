# Random Number Guessing Game

# Write a progam that generates a random number in the range of 1 through 100,
# and asks the user to guess what the number is. If the user's guess is higher
# than the random number, the program should display "Too high, try again."
# If the user's guess is lower than the random number, the application
# should congratute the user and then generate a new random number so the
# game can start over.

# Optinal Enhancement:
# Enhance the game so it keeps count of the number of
# guesses that the user makes. When the user correctly
# guesses the random number, the program should display
# the number of guess.

import random

#Create a function to generate a random number
def genRanNum():
    ran_num = random.randint(1,20)
    return ran_num
#create a function to get user generated number
def askuser():
    while True:
        value = input("Guess a number between 1 - 20: ")
        try:
            value = int(value)
        except ValueError:
            print('Valid Number Please')
            continue
        if 0 < value <= 20:
            return value
        else:
            print('Valid range please: 1-20')

ran = genRanNum() #create an object to hold the random number
miss_count = 0
hit_count = 0

#Create a Main Loop
def guessgame():

while 1 > 0:
    user = askuser()
    if user > ran:
        print("Too High My Guy\nTry Again\n")
        miss_count += 1
        continue
    elif user < ran:
        print("Man, Too Low\nTry Again\n")
        miss_count += 1
        continue
    elif user == ran:
        print("My Friend, That's Correct!\n")
        hit_count += 1
        ans = input('Again? (y or n): ')
        if ans == 'y':
            ran = genRanNum()
            continue
        if ans != 'y':
            break

print("Thanks For Playing!")
print("Number of Misses:",   miss_count,   "Number of Hits:",   hit_count)
