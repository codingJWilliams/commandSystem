#Lottery system
import random,time
def mainProgram():
    correct = ['x','x','x','x','x','x','x']
    numCorrect = 0
    stopProgram = False
    numsint = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    def numChecker(check_string):
        right = 0
        for i in range(7):
            if check_string[i] in numsint:
                right += 1
        if right == 7:
            return True
        else:
            return False
    chosen = []
    userNumbers = input('                             National Lotto! \n   -Please enter your numbers to have a chance of winning the' + ' JACKPOT!\n\n   -Please enter 7 numbers to be in with a chance to win 1,000,000!\nlottery>')
    try:
        userNumbers[7]
    except:
        numCorrect = 1
    if numCorrect == 0:
        print("YOU HAVE TRIED TO CHEAT THE LOTTERY SYSTEM. WOE BETIDE YE")
        stopProgram = True
    else:
        if not numChecker(userNumbers):
            print("YOU HAVE TRIED TO CHEAT THE LOTTERY SYSTEM. WOE BETIDE YE")
            stopProgram = True
    if not stopProgram:
        # Code for the lotto system.
        numCorrect = 0
        chars = []
        for i in range(7):
            chars.append(random.choice(numsint))
        compnum = str(chars[0]) + str(chars[1]) + str(chars[2]) + str(chars[3]) + str(chars[4]) + str(chars[5]) + str(chars[6])
        for a in range(7):
            if compnum[a] == userNumbers[a]:
                numCorrect += 1
                correct[a] = userNumbers[a]
        jsonPrizes = {'0':'nothing, sorry :-(','1':'0 :(','2':'10','3':'50','4':'1000','5':'50,000','6':'250,000','7':'a jackpot of 1,000,000'}
        print("You won:")
        time.sleep(0.5)
        print("*drum-roll*")
        time.sleep(1.5)
        print("You've won {0}, with {1} numbers.\nThe numbers that matched were:\n~{2}".format(jsonPrizes[str(numCorrect)], numCorrect, correct[0] + correct[1] + correct[2] + correct[3] + correct[4] + correct[5] + correct[6]))
    elif stopProgram:
        exit()
