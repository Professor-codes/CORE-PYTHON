number_1 = float(input("Enter number 1: "));  # Convert input to float
number_2 = float(input("Enter number 2: "));  # Convert input to float

operation = ["+", "-", "*", "/", "%"];
print(operation);

op = input("Select operation: ");

if op == "+":
    print("Addition of ", number_1, "+", number_2, " = ", number_1 + number_2);
elif op == "-":
    print("Subtraction of ", number_1, "-", number_2, " = ", number_1 - number_2);
elif op == "*":
    print("Multiplication of ", number_1, "*", number_2, " = ", number_1 * number_2);
elif op == "/":
    print("Division of ", number_1, "/", number_2, " = ", number_1 / number_2);
elif op == "%":
    print("Remainder of ", number_1, "%", number_2, " = ", number_1 % number_2);
else:
    print("Invalid input!");
