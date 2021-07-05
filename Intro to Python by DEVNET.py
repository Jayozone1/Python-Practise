"""myVariable = "This is a global variable"

def myFunction():
    myLocalVariable = "This is a local variable"
    myVariable = "This is a local variable with the same name as the global variable"
    print(myLocalVariable)
    print(myVariable)

myLocalVariable"""



"""b = 5
if b < 0:
    print("b is less than zero")
elif b == 0:
    print("b is exactly zero")
elif b > 2 and b < 7:
    print("b is betwwen three and six")
else:
    print("b is something else")"""


"""names = ["chris", "dave", "bob"]
for j in names:
        print(j)"""

"""i = 5
while i < 4:
    print(i)
    i += 1

while True:
    print("In an infinite loop")"""
"""import math
def circumference(radius):
    result = 2 * 3.14 * radius
    return result

circumference(2)

def say_Hello():
    print("Hello")

say_Hello()"""

import requests
response = requests.get('https://google.com')
response.status_code