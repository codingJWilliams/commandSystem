import random, time
def rnum():
    maxmin = [100,0]
    print("\nWelcome to my random number guessing game, with a twist, of course!\n\nYou will select a number, and python will take a guess, and you will say if it is too high or low!\nLet's have a try!, but make sure your number is between 1 and 100 for now!\n\n1:You Guessed It!\n2:You're too high!\n3:You're too low!")
    while True:
        rnum = random.randint(maxmin[1], maxmin[0])
        results = int(input("Is your number {0}?\noption>".format(rnum)))
        if results == 1:
            print("Yay! I got it! That's so cool! Your number was {0}".format(rnum))
            break
        elif results == 2: maxmin[0] = rnum
        elif results == 3: maxmin[1] = rnum
        else: print("You silly boy or girl. That isn't an option, is it?")
        
