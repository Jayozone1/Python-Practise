"""
###function_demo
#This program demonstates a function.
#First, we define a function named message.

def message():
    print('I am Arthur.')
    print('King of the Britons.')

#call the message function.
message()
"""
"""
##two_functions
#This program has two functions. First we define the main function.
def main():
    print('I have a messgae for you. ')
    message()
    print('Goodbye!')


#Next we define the message function.
def message():
    print('I am Arthut. ')
    print('King of the Britons.')

#calll the main function.
main()
"""
"""
##bad_local
#Definition of the main function.
def main():
    get_name()
    print('Hello', name)     # This causes an error!

# Definition of the get_name function.
def get_name():
    name = input('Enter your name: ')

#call the main function
main()
"""
"""
##Birds.
#This program demonstrates two functions that have local variable with the same name


def main():
    # Call the texas function.
    texas()
    # Call the california function.
    california()

# Definition of the texas function. It creates a local variable named birds.
def texas ():
    birds = 5000
    print('texas has', birds, 'birds.')

#Definition of the california function. It also creates a local variable named birds.
def california():
    birds = 8000
    print('california has', birds, 'birds.')

#Call the main function
main()
"""
"""
##pass_args
#This program demonstrates an argument being passed to a function

def main():
    value = 5
    show_double{value}

#The show_double function accepts an argument and displays double its value
def show_double(number):
    result = number* 2
    print(result)

# Call the main function
main()

"""
"""
##cups_to_ounces
#This program converts cups to fluid ounces


def main():
    #display the intro screen
    intro()
    #Get the number of cups.
    cups_needed = int(input('Enter the numbe rof cups:  '))
    # Convert the cups to onuces.
    cups_to_ounces(cups_needed) 

#The intro function displays an introductory screen.
def intro():
    print('This program converts measurements in cups to fluid ounces.')
    print('For your reference the formula is: 1 cup = 8 fluid ounces)
    print()

#The cups_to_ounces function accepts a number of cupa and displays the eqivalent number of ounces
def cups_to_ounces(cups):
    ounces = cup * 8
    print('That converts to', ounces, 'ounces.')

# Call the main function.
main()
"""
"""
##Multiple_args
#This program demonstrates a function that accepts two arguments

def main():
    print('The sum of 12 and 45 is' )
    show_sum(12, 45)

# The show_sumfunction accepts two arguments and displays their sum.
def show_sum(num1, num2):
    result = num1 + num2
    print(result)

# Call the main function
main()

###String_args
#This program demonstrates passing two string arguments to a function.

def main():
    first_name = input('Enter your first name:  ')
    last_name =  input('Enter yout last name:  ')
    print('Your name reversed is')
    reverse_name(first_name, last_name)

def reverse_name(first, last):
    print(last, first)

# Call the main function
main()
"""
"""
##keyword_args

def main():
    # Show the amount of simple interest, using 0.01 as interest rate per period. 10 as the number of periods.
    # and $10,000 as the principal.
    show_interest(rate=0.01, periods=10, principal=10000.0)
    # The show_interest function displays the amount of simple interst for a given principal, interest rate per period, and number of periods.

def show_interest(principal, rate, periods):
    interest = principal * rate * periods
    print('The simple interest will be $', format(interest, ',.2f'),sep='')

# Call the main function
main()
"""
"""
# This program demonstrates passing two strings as keyword arguments to a function.

def main():
    first_name = input('Enter your first name:  ')
    last_name = input('Enter your last name:  ')
    print('Your name reversed is')
    reverse_name(last=last_name, first=first_name)

def reverse_name(first, last):
    print(last, first)

# Call the main function.
main()
"""
"""
## Global1
#Create a global variable.
my_value = 10

# The show_value function prints the value of the global variable.
def show_value():
    print(my_value)

#call the show_value function
show_value()
"""
"""
##Global2
# Create a global varible.
number = 0

def main():
    global number
    number = int(input('Enter a number: '))
    show_number()

def show_number():
    print('The number you entered is'.  number)

# Call the main function
main()

"""
"""
## Retirement
# The folowing is used as a global constant 
# the contribution rate.
CONTRIBUTION_RATE = 0.05

def main():
    gross_pay = float(input('Enter the gross pay: '))
    bonus = float(input('Enter the amount of bounses: '))
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)

# The show_pay_contrib function accepts the gross pay as an argument and displays the retirement contribution for that amont of pay.
def show_pay_contrib(gross):
    contrib = gross * CONTRIBUTION_RATE
    print('Contribution for gross pay: $', format(contrib, ',.2f'), sep='')

# The show_bonus_contrib function accepts the bonus amount as an argument and displays the retirement contribution for that amount of pay.
def show_bonus_contrib(bonus):
    contrib = bonus * CONTRIBUTION_RATE
    print('Contribution for bonuses: $', format(contrib, ',.2f'), sep='')

# Call the main function.
main()
"""
"""
##Random_numbers
#This program displays a random number in the range of 1 through 10.
import random

def main():
    #Get a random number.
    number = random.randint(1, 10)
    # Display the number
    print('The number is'. number)

# Call the main function.
main()

"""
"""
##random_numbers
#This program displays five random numbers in the range of 1 through 100
import random

def main():
    for count in range(5):
        #Get a random number.
        number = random.randint(1, 100)
        #Display the number
        print(number)

#Call the main function.
main()
"""
"""
## random_numbers3
# This program displays five random numbers in the range of 1 through 100
import random

def main():
    for count in range(5):
        print(random randint(1, 100))

# Call the main function.
main()
"""
"""
##Dice
#This program the rolling of dice
import random

#Constants fpr the minimum and maximum random numbers
MIN = 1
MAX = 6

def main():
    #Create a variable to control the loop.
    again = 'y'


    #Simulate rolling the dice.
    while again == 'y' or again == 'Y':
        print('Rolling the dice.....')
        print('Their values are:')
        print(random.randint(MIN, MAX))
        print(random.randint(MIN,MAX))

        #Do another rol of the dice?
        again = input('Roll them again? (y = yes): ')

# Call the main function
main()
"""
"""
##Coin_toss
#This program simulaes 10 tosses of a coin.
import random

#Constants
HEAD = 1
TAILS = 2
TOSSES = 10
def main():
    for toss in range(TOSSES):
        #Simulate the coin toss.
        if random.randint(HEADS, TAILS) == HEADS:
            print('Heads')
        else:
            print('Tails')

# Call the main function.
main()
"""
"""
##TOTAL_AGES
#This program uses the return value of a function

def main():
    # Get the user's age.
    first_age = int(input('Enter your age: '))

    #Get the user's best friend's age.
    second_age = int(input("Enter your best friend's age: "))

    #Get the sum of both ages.
    total = sum(first_age, second_age)

    #Display the total age.
    print('Together you are', total, 'years old.')

#The sum function accepts two numeric arguments and returns the sum of those arguments.
def sum(num1, num2):
    result = num1 + num2
    return result

# Call the main function
main()
"""
"""
##Sale_price
#This program calculates a retail item's sale price

#DISCOUNT_PERCENTAGE is used as a global constant for the discount percentage.
DISCOUNT_PERCENTAGE - 0.20

#The main function
def main():
    #Get the item's regular price.
    reg_price = get_regular_price()

    #Calculate the sale price.
    sale_price - dicount(reg-price)

    #Display the sale price.
    print('The sale price is $', format(sale_price, ',.2f'), sep='') 
# The get_regular_price function prompts the user to enter an item's regular price and it returns that value.
def get_regular_price():
    price = float(input("Enter the item's regular price:  "))
    return price
# The discount function accepts an item's price as an argument and returns the amount of the discount specified by DISCOUNT_PERCENTAGE.
 def discount(price):     
  return price * DISCOUNT_PERCENTAGE 
# Call the main function. 
#   main()
"""
"""
##commission_rate.
 # This program calculates a salesperson's pay 
# at Make Your Own Music. 
     def main(): 
           # Get the amount of sales.    
           sales = get_sales() 
           
          # Get the amount of advanced pay. 
          advanced_pay = get_advanced_pay() 
          
          # Determine the commission rate. 
           comm_rate = determine_comm_rate(sales) 
               
          # Calculate the pay. 
           pay = sales * comm_rate − advanced_pay 
           
         # Display the amount of pay. 
           print('The pay is $', format(pay, ',.2f'), sep='') 
           
         # Determine whether the pay is negative. 
           if pay < 0: 
             print('The Salesperson must reimburse') 
             print('the company.') 

"""
"""
##  (Commission_rate) get_sales function
#The get_sales function gets a saleperson's monthly sales from the user and returns that value
def get_sales():
    #Get the amount of monthly sales.
    monthly_sales = float(input('Enter the monthly sales:  '))

    # Return the amount entered.
    return monthly_sales
"""

"""
##Square_root
#This program demonstrates the sqrt function.
import math

def main():
    #Get a number.
    number = float(input('Enter a number:  '))

    #Get the square root of the number.
    square_root = math.sqrt(number)

    #Display the square root.
    print('The square root', number, '0 is', square_root)

# Call the main function
main()
"""
"""
##Hypotenuse
#This program calculates the length of a right triangle's hypotenuse.
import math

def main():
    #Get the length of the triangle's two sides.
    a = float(input('Enter the length of side A:  '))
    b = float(input('Enter the length of side B:   '))

    #Calculate the length of the hypotenuse.
    c = math.hypot(a, b)

    #Display the length of the hypotenuse.
    print('The lenght of the hypotenuse is', c)

#Call the main function
main()
"""
"""
##Circle
#The circle module has functions that perform calculatons relate to circles.
import math

#The are function accepts a circle's radius as an argument and returns the area of the circle.
def area(raduis):
    return math.pi * raduis ** 2
    #The circumference function accepts a circle's radius and return the circle's circumfeenc.
    def circumference(raduis)
        return 2 * math.pi * raduis
"""
"""
##Rectangle
#The rectangle module has functions that parform calculations related to rectangles.
#The area function accepts a rectangle's width and length as arguments and returns the rectangle's area.
def area(width, length):
    return width * length

#The perimater function accepts a rectangle's width and length as argu,ments and returns the rectangle's perimeter
def perimeter(width, length):
    return 2 * (width + length)
"""
"""
##Geometry
#This program allows the user to choose various geometry calculations from a menu. This program imports the circl and the rectangles modules.
import circle
import rectangle

#Constants for the menu choice
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE =  2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

#The main function.
def main():
    #The choice variable controlas the loop and holds the user's menu chioce.
    choice = 0

    while choice != QUIT_CHIOCE:
        #display the menu()

        #Get the user's choice.
        choice = int(input('Enter your choice:  '))

        #Perform the selcted action.
        if choice == AREA_CIRCLE_CHOICE:
            raduis = float(input("Enter the circle's raduis:  "))
            print('The area is'. circle.area(raduis))
        elif choice == CIRCUMFERENCE_CHOICE:
            raduis = float(input("Enter the circle's radius:  "))
            print('The circumference is'. circle.circumference(raduis))
        elif choice == AREA_RECTANGLE_CHOICE:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print('The ara is', rectangle.area(width,length))
        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input("Enter the rectangle's width:  "))
            length = float(input("Enter the rectangle's length: "))
            print('The perimeter is', rectangle.perimeter(width, length))
        elif choice ==QUIT_CHOICE:
            print('Exiting the program....')
        else:
            print('Error: invalid selcetion.')

#The display_menu function displays a menu.
def display_menu():
    print('MENU')
    print('1) Area of a circle')
    print('2) circumference of a circle')
    print('3) Area of a rectangle')
    print('4) Perimeter of a rectangle')
    print('5) Quit')

# Call the main function
main()
"""