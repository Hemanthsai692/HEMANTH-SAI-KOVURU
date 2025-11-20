class Calculator:
    def calculate(self, a, b, operation):
        if operation == "add":
            return a + b
        elif operation == "sub":
            return a - b
        elif operation == "mul":
            return a * b
        elif operation == "div":
            if b == 0:
                return "Cannot divide by zero"
            return a / b
        else:
            return "Invalid operation"
a = float(input("Enter a: "))
b = float(input("Enter b: "))
op = input("Enter operation (add/sub/mul/div): ")
calc = Calculator()
print("Result:", calc.calculate(a, b, op))

