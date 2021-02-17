import random

#The coin class simulates a coin that can be flippes.

class Coin:

    #The __init__ method initializes the __sideup data attribute with 'Heads'.

    def __init__(self):
        self.__sideup = 'Heads'

    #The toss method generatas a random number in the range of 0 through 1. If the number is 0, then sideup is set to 'Heads'. otherwise, sideup is set to 'Tails'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Head'
        else:
            self.__sideup = 'Tails'
    # The get_sideup method returns the value referenced by sideup.

    def get_sideup(self):
        return self.__sideup