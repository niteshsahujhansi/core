import math
import random
import sys

def main():

    # taking the range(lower, upper) of the number 
    lower = int(input('Enter lower bound: '))
    upper = int(input('Enter upper bound: '))

    # generating random integer between the range 
    x = random.randint(lower, upper)

    # calculate minimum no of chances in which one can guess the integer number successfully  
    chances = round(math.log(upper - lower + 1 , 2))

    # shows the no of chances that user have in order to guess the integer
    print('You have only ', chances, ' chances to guess the integer')

    # initialize the counter that will be compared with the no of chances 
    count = 0

    # run loop until the user exceeds the number of chances to guess the integer
    # or the user guesses successfully 
    while (count < chances) :

        # take guess integer input
        guess = int(input('Enter your guess: '))

        # check if guess is successful, small or high and print statements accordingly  
        if x == guess :
            print('Congratulations you did it')
            break 

        elif guess < x :
            print('Your guess is too small')
            
        elif guess > x :
            print('Your guess is too hight')
            
        # increment the counter by 1
        count += 1

    # if the user exceeds the number of chances to guess the integer show statement accordingly  
    if count >= chances :
        print('The number is ',x)
        print('Batter luck next time')

def exit_or_play() :
    while(True):
        y = input('Do you want to play again (y/n) : ')
        if y == 'y' :
            main()
        else:
            return False 

main()
exit_or_play()
