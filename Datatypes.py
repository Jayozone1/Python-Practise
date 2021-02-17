"""x = 75.0
print( 'x is {}'.format(x) )

print(type(x))"""

"""x = f'hello world {0} {1}'
print ( 'x is {}'. format(x))

print(type(x))"""


"""from decimal import *

a = Decimal('.1')
b = Decimal('.3')


x = a + a + a - b


print(   'x is {}'.format(x))

print(type(x))"""


"""x = ' '

print(  'x is  {}'.format(x) ) 


if x:
    print('True')
else:
    print('False')


print(type(x))"""


# x = [1, 2, 3, 4, 5] # List
# x = (1, 2, 3, 4, 5)# Tuple
# x  = range(5) #Range
# x = range(5, 10) # Range (From & To)
# x = range(5, 50, 5) # Range(From , To, Step)


# x = list(range(5))  # Range
# x[2] = 42

"""x = { 'one':1, 'two':2, 'three':3, 'four':4, 'five':5 }
x['two'] = 'fifty five'
for id, value in x.items():
     print('id: {}, value:{}'.format(id, value))

x = range(5, 50, 5) # Range (From & To)
#x[2] = 34

for i in x:
     print(i)"""

# type(x)
# id(x)
# isInstance(x, tuple or list)


"""x = (1, 'two', 3.0, [4], 5)
y = [1, 'two', 3.0, [4], 5]

if isinstance(y, tuple):
    print('Tuple')
elif isinstance(y, list):
    print('List')
else:
    print('something')"""


"""x = 0.1


if x < 50:
    print( 'x is <  50')
elif x == 50:
    print( 'x is  == 50')
elif x > 50:
    print( 'x is > 50')
else:
    print( 'something')"""

"""Ishungry = False


x = 'I need lunch' if Ishungry  else 'I need some Tea'

print(x)"""


"""#Arithmetic Operation

x = 25
y = 75
z = x + y

print('The Result  is {}'.format(z))"""

"""x = 75
y = 25

if x == y:
    print(' True' )
else:
    print( 'False')"""


"""a = True
b = False
x = ( 'dogs', 'cats', 'rabbits', 'hamsters', 'birds')
y = 'cats'

if  a is b:
    print( 'Expression is true')
else:
    print( 'Expression is false')"""


"""password = '123'
pw = ''

while pw in password:
    pw = input('what is the password? ')"""

#For Loop
"""pets = ( 'dogs', 'cats', 'rabbits', 'hamsters', 'birds' )


for pet in pets:
    print('I need {}'.format(pet))"""


#Loop Control in Python
"""password = '123'
pw = ''
auth = False
count = 0
max_attempt = 5


while pw is password:
    count = count + 1
    if count > max_attempt:
        break
    pw = input(f'{count}: what is the password? ')
else:
    auth = True

print('Authorized' if auth else 'Account locked' )"""

"""def main():
    x = runMe()
    print(x)


def runMe():
    return 'I am running'


if __name__ == '__main__':
    main()"""

"""def main():
    runMe(5, 25)

def runMe(x=0, y=0, z=0):
    print( 'I am running' )
    print(x, y, z)
    print()


if __name__ == "__main__":
    main()"""


"""def main():
    runMe(0, 5)


def runMe():
    while x < y:
        print(f'{x} is the value')
        x = x + 1
if __name__ == "__main__":
    main()"""
#List
"""def main():
    people('John', 'Jane', 'Smith', 'Rahel', 'Raj')

def people(*args):
    if len(args):
        for name in args:
            print(name)
    else:
        print('Nobody')

if __name__ == "__main__":
    main()"""

#Keywords Argument
"""def main():
    people( john='Hello', jane='Hi',smith='Hey' )

def people(**kwargs):
    if len(kwargs):
        for name in kwargs:
            print( f'{name} says {kwargs[name]}' )
    else:
        print('Nobody')

if __name__ == "__main__":
    main()"""

#Return Values Function
"""def main():
    x = runMe()
    print(type(x), x)


def runMe():
    print('Nice Program')
    return dict( x='25', y='50', z='70')

if __name__ == "__main__":
    main()"""


##Generators##
def main():
    for i in range(10):
        print (i, end=' ')
    print()

def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1

    #initialize parameters
    if numargs < 1:
        raise TypeError(f'expected at least 1 argument {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError(f'expected at most 3 arguments, get {numargs}')
    #generator
    i = start
    while i <= stop:
        yield 1
        i = i + step

if __name__ = "__main__"
    main()