input("Press enter to begin :")
print("------------------------")

allowed_operators = ["+", "-", "/", "*"]

def get_number(prompt):
    while True:
        value = input(prompt)

        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number")


def get_operator():

    while True:
        operator_input = input("Enter operator : ")

        if operator_input in allowed_operators:
            return operator_input

        print("Please enter a valid operator (+, -, /, *)")

while True:

    number_one = get_number("Please enter a number : ")
    operator_input = get_operator()
    number_two = get_number(f"Please enter your second number e.g {number_one} {operator_input}  : ")

    if operator_input == "+":
        result = (number_one) + (number_two)
        print("------------------------")
        print(f"{result}")
        print("------------------------")
    elif operator_input == "-":
        result = (number_one) - (number_two)
        print("------------------------")
        print(f"{result}")
        print("------------------------")
    elif operator_input == "*":
        result = (number_one) * (number_two)
        print("------------------------")
        print(f"{result}")
        print("------------------------")
    elif operator_input == "/":
        if number_two == 0:
            print("------------------------")
            print("Cannot divide by zero")
            print("------------------------")
            again = input("Would you like to calculate again? (yes/no) : ").lower()
            print("------------------------")
            if again == "no":
                break

            continue

        result = (number_one) / (number_two)
        print("------------------------")
        print(f"{result}")
        print("------------------------")

    again = input("Would you like to calculate again? (yes/no) : ").lower()
    print("------------------------")
    if again == "no":
        break


