import random

#The coin class simulates a coin that can be flipped.

class Coin:

     #The  __init__ method initializes the __sideup data attribute with 'Heads'.
    def __init__(self):
        self.__sideup = 'Heads'
    
    #The toss method generates a random number in the range of 0 throgh 1. if the number is 0, then sideip is set to 'Heads', otherwise, sidep is set to 'Tails'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    #The get_sideup method returns the value referenced by sideup.

    def get_sideup(self):
        return self.__sideup

#The main function.
def main():
    #Create an object from Coin class
    my_coin = Coin()

    #Display the side of the coin that is facing up.
    print('This side is up:', my_coin.get_sideup())

    #Toss the coin.
    print('I am goin to toss the coin ten times:')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

# Call the main function.
main()
