"""The Number Guessing Game
The goals were to make a game where the user has to guess a number and it gets progressively harder
the project asks the user for a difficulty level then based on that a function creates a number for the user to remember
and a time for the user to have for the guess, after the user remembers the number 3 times the difficulty increases"""
import time #import the time module 
import os #imports the os module 
import secrets #imports the secrets module 

difficulty = int(input("Choose a difficulty 1-10: ")) #asks the user for a choice in difficulty 1-10 

def Difficulty_generator(difficulty): #makes a function that returns the number size and time that the number is shown for the game 
    if difficulty == 1:
        Time = .5
        Number = secrets.choice(range(1, 10))
    elif difficulty == 2:
        Time = .5
        Number = secrets.choice(range(10, 100))
    elif difficulty == 3:
        Time = .5
        Number = secrets.choice(range(100, 1000))
    elif difficulty == 4:
        Time = .6
        Number = secrets.choice(range(1000, 10000))
    elif difficulty == 5:
        Time = .7
        Number = secrets.choice(range(10000, 100000))
    elif difficulty == 6:
        Time = .9
        Number = secrets.choice(range(100000, 1000000))
    elif difficulty == 7:
        Time = 1
        Number = secrets.choice(range(1000000, 10000000))
    elif difficulty == 8:
        Time = 1.2
        Number = secrets.choice(range(10000000, 100000000))
    elif difficulty == 9:
        Time = 1.3
        Number = secrets.choice(range(100000000, 1000000000))
    elif difficulty == 10:
        Time = 1.4
        Number = secrets.choice(range(1000000000, 10000000000))
    return Number, Time

streak = 0 #makes a streak, value of 0 to start 

while True: # creates a loop that wont be broken until the user uses q to quit the game 
    Number, Time = Difficulty_generator(difficulty) #assigns Number and Time for the game based on the difficulty if loop 

    print("Difficulty: ", difficulty) #prints out the level of difficulty 
    os.system('cls') #clears the console 

    print("Number to remember: ", Number) #prints the number the user has to remember 
    time.sleep(Time) # uses the time from the 

    os.system('cls') #clears the console 

    Guess = input("Enter the number you saw: ") #makes a guess input of the number the user guessed 
    result = int(Guess) == Number # assigns result the value of guess as an int 
    if result == True: # if the user guesses the number correctly 
        print("Correct")  #prints correct if the number was guessed correctly 
    else:
        print("Incorrect, the number was: ", Number) #tells the user theyre wrong and sends the number that was correct 

    if result: # if the result is true 
        streak += 1 #adds one to the streak 
        if streak == 3:  #if the user gets the guesses correctly 3 times then the difficulty is increased by a level 
            if difficulty < 10: #if difficulty is below 10  add another level of difficulty 
                difficulty += 1
                print("Difficulty now: ", difficulty) #tells the user the difficulty 
            else: #
                print("Maximum Difficulty") #tells the user they are at max difficulty or level 10 
            streak = 0 # resets the streak on the next level 


    again = input("Press Enter to continue or type 'q' to quit: ") #creates a variable, again 
    if again.lower() == 'q': #if the value of again is q then the loop breaks and the game is over 
        break
print("Thank you for playing!") 
