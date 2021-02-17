#This program demonstrates the Car class.

import vechicles

def main():
    #Create an object from the car class. The car is a 2007 Audi with 12,500 miles,
    #priced ar $21,500 and  has 4 doors.
    used_car = vechicles.Car('Audi', 2007, 12500, 21500.0, 4)

    #Display the car's data.
    print('Make:', used_car.get_make())
    print('Model:', used_car.get_model())
    print('Milage:', used_car.get_milage())
    print('Price:', used_car.get_price())
    print('Number of doors:', used_car.get_doors())

#Call the main function
main()