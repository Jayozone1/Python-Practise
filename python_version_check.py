import platform

def main():
    message()

def message():
    print( 'This is a python version {}' .format( platform.python_version() ) )
    print("This is Hello World")
    print("Bye World")
    if True:
    print( 'True')
    else:
    print( 'False')


if __name__  == "__main__":
    main()