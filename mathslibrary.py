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
