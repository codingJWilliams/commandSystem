import random
import time
import hashlib
import json
import mathslibrary
debug = True
# A program designed to emulate a windows pc.
class auth():
    def auth():
        with open('logins.json') as f:    
            s = f.readlines()[0]
            logins = json.loads(s)
            if debug:
                print("Logins = {0} at read".format(s))
            f.close()
        username = input("\n\n +----+ Secure login prompt +----+\nUsername >")
        try:
            logins[username][1]
            print("Got hash from DB")
        except KeyError:
            print("Incorrect username.\n +----+ [              ] +----+")
            return False
        except:
            print("Error - Code 1.")
        else:
            print("Username correct.")
            userpasshash = hashlib.sha256(str(input("Password >")).encode('utf-8')).hexdigest()
            print("passhash = {0}".format(userpasshash))
            if userpasshash == logins[username][1]:
                print(" +----+      Thank You!      +----+")
                return logins[username][0]
            else:
                return False
        logins = {}
    def adduser():
        with open('logins.json') as f:
            s = f.readlines()[0]
            logins = json.loads(s)
            f.close()
        print()
        username = input("Please choose a username!\nusername>")
        passwdhash = hashlib.sha256(str(input("Please choose a password!\npassword>")).encode('utf-8')).hexdigest()
        logins[username] = [username, passwdhash]
        outfile = open("logins.json", "w")
        outfile.write(json.dumps(logins))
def pc(frrun):
    if frrun == 1:
        print("Welcome to this computer-style program. \n\n\n")
    login = auth.auth()
    if login is not False:
        #user is authed
        print("\nPlease enter a command!") 
        while True:
            cmd = input("{0}>".format(login))
            if cmd.lower() == 'logout':
                break
            elif cmd.lower() == 'exit':
                exit
            elif cmd.lower() == 'calc':
                mathslibrary.calc()
            elif cmd.lower() == 'adduser':
                auth.adduser()
            else:
                print('Invalid command! Try typing \"help\"')
    elif login is False:
        #user is not authed
        print("Login Incorrect")
pc(1)
while True:
    pc(0)

