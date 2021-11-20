# addition
# subtraction
# multiplication
# division
whil=True

while(whil):
    op= int(input("""Please enter an option
                1. addition
                2. subtraction
                3. multiplication
                4. division
                5. exit
    """))
    if op == 1:
        number1 = float(input("Please enter u first number "))
        number2 = float(input("Please enter u second number "))
        print("Result: ",number1+number2)
    elif op == 2:
        number1 = float(input("Please enter u first number "))
        number2 = float(input("Please enter u second number "))
        print ("Result: ",number1-number2)
    elif op == 3:
        number1 = float(input("Please enter u first number "))
        number2 = float(input("Please enter u second number "))
        print("Result: ",number1*number2) 
    elif op == 4:
        number1 = float(input("Please enter u first number "))
        number2 = float(input("Please enter u second number "))
        print("Result: ",number1/number2)
    elif op==5:
        whil=False
    else:
        print("Please enter a valid option. Error")
