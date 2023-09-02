class Calculator:

    def __init__(self):
        self.total = 0
        first = float(input("Enter Number = "))
        self.total = self.total + first
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
            exit()

    def addition(self):
        a = float(input("Enter number = "))
        self.total = self.total + a
        print("TOTAL = ", self.total)
        self.menu()

    def subtraction(self):
        a = float(input("Enter Number = "))
        self.total = self.total - a
        print("TOTAL = ", self.total)
        self.menu()

    def multiplication(self):
        a = float(input("Enter number = "))
        self.total = self.total*a
        print("TOTAL = ", self.total)
        self.menu()

    def division(self):
        a = float(input("Enter number = "))
        if a == 0:
            print("Cannot Be Divided By 0")
        else:
            self.total = self.total/a
            print("TOTAL = ", self.total)

        self.menu()


obj = Calculator()