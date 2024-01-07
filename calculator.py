def main():

    loop = 1

    while loop == 1:
        print("--------------------------CALCULATOR--------------------------")
        print("Select an Operation")
        print("1. Addition")
        print("2. Substraction")
        print("3. Multiplication")
        print("4. Division")

        cal = int(input("SELECT: "))

        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))

        if cal == 1:
            print("You have selected addition")
            print("Total: ", int(x)+int(y))

        elif cal == 2:
            print("You have selected substraction")
            print("Total: ", int(x)-int(y))

        elif cal == 3:
            print("You have selected multiplication")
            print("Total: ", int(x)*int(y))

        elif cal == 4:
            print("You have selected division")
            print("Total: ", int(x)/int(y))

        else:
            "--------------------------Thank you for using the calculator--------------------------"
            exit()

main()