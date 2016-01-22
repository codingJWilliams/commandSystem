import random
import time
import hashlib
import json
import mathslibrary
import lottery
import os
import rnum
import fileutils
#Below is where you assign commands, so you can easily add commands in the format demonstrated
def commandAssignment(logit):
    cmd = input("{0}>".format(logit))
    if cmd.lower() == 'logout':
        return True
    elif cmd.lower() == 'backup':		
        name = input("Please enter the backup name:\nbackup>")		
        with open('logins.json') as f:		
            s = f.readlines()[0]		
            logins = json.loads(s)		
            f.close()		
        outfile = open("logins_backup_{0}.json".format(name), "w")		
        outfile.write(json.dumps(logins))		
        outfile.close()
    elif cmd.lower() == 'exit':
        return "exit"
    elif cmd.lower() == 'calc':
        try: mathslibrary.calc()
        except: print("error> Program crashed. Returning to prompt.")
    elif cmd.lower() == 'randomnumber':
        try: rnum.rnum()
        except: print("error> Program crashed. Returning to prompt.")
    elif 'adduser' in cmd.lower():
        if cmd.lower().split(" ")[0] == 'adduser':
            args = cmd.lower().split(" ")[1:]
            if not len(args) == 2:
                print("error> Please provide the username and password like \"adduser name pass\"")
                return
            auth.adduser(args[0], args[1])
            print("adduser> User {0} added.".format(args[0]))
        else:
            print('Invalid command! Try typing \"help\"')
    elif cmd.lower() == 'auth':
        try: print("Logged in as {0}".format(auth.auth()))
        except: print("error> Program crashed. Returning to prompt.")
    elif cmd.lower() == 'help':
        getHelp()
    elif cmd.lower().split(" ")[0] == 'file':
        try:
            if cmd.lower().split(" ")[1] == 'touch':
                fileutils.touch(cmd.lower().split(" ")[2])
            elif cmd.lower().split(" ")[1] == 'read':
                fileutils.printFile(cmd.lower().split(" ")[2])
            elif cmd.lower().split(" ")[1] == 'write':
                fileutils.writeTo(cmd.lower().split(" ")[2], str.join(" ", cmd.lower().split(" ")[3:]))
            elif cmd.lower().split(" ")[1] == 'del':
                if os.path.isfile(cmd.lower().split(" ")[2]):
                    os.remove(cmd.lower().split(" ")[2])
                    print("file> removed {0}".format(cmd.lower().split(" ")[2]))
                else:
                    print("error> file does not exist")
        except IndexError:
            print("error> arguments")
        except:
            print("error> unknown")
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
class auth():
    def auth():
        if not os.path.isfile("logins.json"):
            print("error> logins.json is not found. To fix this, find instructions on my Git repo.\n\n\n")
            print("\n\n\nlogins.json was not found in the same folder as main.py. Please rename one of the backups you created or exit the program and follow the instructions on my git to make a new file")           
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
    def adduser(username, password):
        with open('logins.json') as f:
            s = f.readlines()[0]
            logins = json.loads(s)
            f.close()
        print()
        passwdhash = hashlib.sha256(str(password).encode('utf-8')).hexdigest()
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

