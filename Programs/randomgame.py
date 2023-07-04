#generate a number 1-10
#input from the user
#check the input is a number 1-10
#check if number is the right guess. Otherwise
#ask again

from random import randint
import sys

answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        print(answer)

        guess = int(input("Guess a number between 1 to 10:  "))

        if guess > 0 and guess < 11:

            if guess == answer:
                print("You are a genius")
                break
        else:
            print("Hey..I said a number btw 1 to 10")
    except ValueError:
        print("Please enter a number")
        continue





