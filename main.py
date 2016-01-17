import random
import time
import hashlib
import json
import mathslibrary
import lottery
import os
import rnum
#Below is where you assign commands, so you can easily add commands in the format demonstrated
def commandAssignment(logit):
    cmd = input("{0}>".format(logit))
    if cmd.lower() == 'logout':
        return True
    elif cmd.lower() == 'exit' or 'quit':
        return "exit"
    elif cmd.lower() == 'calc':
        try:
            mathslibrary.calc()
        except:
            print("error> Program crashed. Returning to prompt.")
    elif cmd.lower() == 'randomnumber':
        try:
            rnum.rnum()
        except:
            print("error> Program crashed. Returning to prompt.")
    elif cmd.lower() == 'adduser':
        try:
            auth.adduser()
        except:
            print("error> Program crashed. Returning to prompt.")
    elif cmd.lower() == 'auth':
        try:
            print("Logged in as {0}".format(auth.auth()))
        except:
            print("error> Program crashed. Returning to prompt.")
    elif cmd.lower() == 'help':
        getHelp()
    elif cmd.lower() == 'lottery':
        try:
            lottery.mainProgram()
        except:
            print("error> Program crashed. Returning to prompt.")
    else:
        print('Invalid command! Try typing \"help\"')




# Body of program

debug = False
# A program designed to emulate a windows pc.
def getHelp():
    print(" +----+ [ Help Prompt ] +----+ ")
    print("Authentication:")
    print(" logout - Logs off so you can log in as another person")
    print(" adduser - Adds a user to the login file so they can then log in.")
    print(" auth - Shows a login prompt for testing purposes.")
class Oopsy(Exception):
    pass
def argGetter(string):
    splitted = string.split(" ")
    return splitted[1:]
class auth():
    def auth():
        if not os.path.isfile("logins.json"):
            print("error> logins.json is not found. To fix this, find instructions on my Git repo.\n\n\n")
            raise Oopsy("\n\n\nlogins.json was not found in the same folder as main.py. Please rename one of the backups from logins_backup_name.json to logins.json.")
            return False
        with open('logins.json') as f:
            try:
                s = f.readlines()[0]
            except IndexError:
                print("error> logins.json is empty. Please restore from backup or follow instructions to fix it, which can be found on my Git Repo.\n\n\n")
                quit()
            logins = json.loads(s)
            if debug:
                print("Logins = {0} at read".format(s))
            f.close()
        username = input("\n\n +----+ Secure login prompt +----+\nUsername >")
        try:
            logins[username][1]
            if debug:
                print("Got hash from DB")
        except KeyError:
            print("Incorrect username.\n +----+ [              ] +----+")
            return False
        except:
            print("Error - Code 1.")
        else:
            print("Username correct.")
            userpasshash = hashlib.sha256(str(input("Password >")).encode('utf-8')).hexdigest()
            if debug:
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
            answer = commandAssignment(login)
            if answer == True:
                break
            elif answer == "exit":
                quit()
    elif login is False:
        #user is not authed
        print("Login Insuccessful")
        quit()
pc(1)
while True:
    pc(0)

