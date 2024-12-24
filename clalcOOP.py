class Calculator:
    def __init__(self):
        pass
    def Add(self, a, b):
        return a + b
    def Subtract(self, a, b):
        return a - b
    def Multiply(self, a, b):
        return a * b
    def Divide(self, a, b):
        return a / b

def main():
    while True:
        print("Choose the operation")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Exit")
        userChoise = int(input("Enter your choice: "))

        if userChoise == 5:
            return

        firstNumber = int(input("Enter first number: "))
        secondNumber = int(input("Enter second number: "))

        calc = Calculator()

        if userChoise == 1:
            print(calc.Add(firstNumber, secondNumber))
        elif userChoise == 2:
            print(calc.Subtract(firstNumber, secondNumber))
        elif userChoise == 3:
            print(calc.Multiply(firstNumber, secondNumber))
        elif userChoise == 4:
            if secondNumber == 0:
                print("Devision by zero is not allowed!")
            else:
                print(calc.Divide(firstNumber, secondNumber))

main()
# comments
# comment2 2.0
# comment 3.0