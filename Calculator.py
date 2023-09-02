class Calculator:

    def __init__(self):
        self.total = 0
        try:
            first = float(input("Enter Number = "))
            self.total = self.total + first

        except ValueError:
            print("Invalid Input!! Please Try Again With A Valid Input")
            Calculator()

        self.menu()


    def menu(self):
        user_input = input("""
        MENU
        <> +
        <> -
        <> *
        <> /
        <> PRESS ANY OTHER KEY TO EXIT
        """)

        if user_input == "+":
            self.addition()
        elif user_input == "-":
            self.subtraction()
        elif user_input == "*":
            self.multiplication()
        elif user_input == "/":
            self.division()
        else:
            print("Result = ", self.total)
            exit("THANK YOU FOR USING")


    def addition(self):
        try:
            a = float(input("Enter number = "))
            self.total = self.total + a
            print("TOTAL = ", self.total)

        except ValueError:
            print("Invalid Input!!!! Please Try Again With Valid Input")

        self.menu()

    def subtraction(self):
        try:
            a = float(input("Enter Number = "))
            self.total = self.total - a
            print("TOTAL = ", self.total)
            self.menu()

        except ValueError:
            print("Invalid Input!!!! Please Try Again With Valid Input")

        self.menu()

    def multiplication(self):
        try:
            a = float(input("Enter number = "))
            self.total = self.total*a
            print("TOTAL = ", self.total)
            self.menu()

        except ValueError:
            print("Invalid Input!!!! Please Try Again With Valid Input")

        self.menu()
    def division(self):
        try:
            a = float(input("Enter number = "))
            self.total = self.total/a
            print("TOTAL = ", self.total)
            self.menu()

        except ZeroDivisionError:
            print("Cannot Divide With 0!!! Please Try Again")

        except ValueError:
            print("Invalid Input!!!! Please Try Again With Valid Input")

        self.menu()





obj = Calculator()