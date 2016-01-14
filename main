import random
import time
import hashlib
import json
import mathslibrary
# A program designed to emulate a windows pc.
class auth():
    def auth():
        with open('logins.json') as f:    
            s = f.readlines()[0]
            logins = json.loads(s)
            f.close()
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
        logins = {}
    def adduser():
        with open('logins.json') as f:
            s = f.readlines()[0]
            logins = json.loads(s)
            f.close()
        print()
        username = input("Please choose a username!\nusername>")
        logins[username] = input("Please choose a password!\npassword>")
        outfile = open("logins.json", "w")
        outfile.write(json.dumps(logins))
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
                mathslibrary.calc()
            elif cmd.lower() == 'adduser':
                auth.adduser()
            else:
                print('Invalid command! Try typing \"help\"')
    elif login is False:
        #user is not authed
        quit()
pc()

