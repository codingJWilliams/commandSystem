import random
import time
import hashlib
import json
# A program designed to emulate a windows pc.
with open('logins.json') as f:    
    s = f.readlines()[0]
    logins = json.loads(s)
class maths():

    def add():
        print("Enter the two numbers to Add")
        A = float(input("a>"))
        B = float(input("b>"))
        return A + B 

    def sub():
        print("Enter the two numbers to Subtract")
        A = float(input("a>"))
        B = float(input("b>"))
        return A - B

    def mul():
        print("Enter the two numbers to Multiply")
        A = float(input("a>"))
        B = float(input("b>"))
        return A * B

    def div():
        print("Enter the two number to Divide")
        A = float(input("a>"))
        B = float(input("b>"))
        return A / B

    def calc():
        print("\n1: ADDITION")
        print("2: SUBTRACTION")
        print("3: MULTIPLICATION")
        print("4: DIVITION")
        print("0: QUIT")
        CHOICE = int(input("\nchoice>")) 

        if CHOICE == 1: 
            print('ADDING TWO NUMBERS:')
            print(round(maths.add(), 5))
        elif CHOICE == 2:
            print('SUBTRACTING TWO NUMBERS')
            print(round(maths.sub(), 5))
        elif CHOICE == 3:
            print('MULTIPLYING TWO NUMBERS')
            print(round(maths.mul(), 5))
        elif CHOICE == 4:
            print("DIVIDING TWO NUMBERS")
            print(round(maths.div(), 5))
        elif CHOICE == 0:
            pass
        else:
            print("Enter value from 1-4")
class auth():
    def auth():
        username = input(" +----+ Secure login prompt +----+\nUsername >")
        try:
            logins[username][1]
        except KeyError:
            print("Incorrect username.\n +----+ [              ] +----+")
            return False
        except:
            print("Error - Code 1.")
        else:
            print("Username correct.")
            userpasshash = hashlib.sha256(str(input("Password >")).encode('utf-8')).hexdigest()
            if userpasshash == logins[username][1]:
                print(" +----+      Thank You!      +----+")
                return logins[username][0]
            else:
                return False
    #def adduser():
    #    print()
    #    username = input("Please choose a username!\nusername>")
    #   logins[username] = input("Please choose a password1\npassword>")
    #    with open('logins.json', 'w') as outfile:
    #        json.dump(data, logins)
def pc():
    print("Welcome to this computer-style program. \n\n\n")
    login = auth.auth()
    if login is not False:
        #user is authed
        print("\nPlease enter a command!")
        while True:
            cmd = input("{0}>".format(login))
            if cmd.lower() == 'exit':
                break
            elif cmd.lower() == 'calc':
                maths.calc()
            elif cmd.lower() == 'adduser':
                auth.adduser()
            else:
                print('Invalid command! Try typing \"help\"')
    elif login is False:
        #user is not authed
        quit()
pc()
