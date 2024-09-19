from ascii import icon


# TODO 1: Making the function for all possible operation
def addition(n1, n2):
    return n1 + n2


def subtraction(n1, n2):
    return n1 - n2


def multiplication(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


# TODO 2: Assigning the function to the dictionary
operations = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division,
}


# TODO 6: Assigning the calculator as a function so it can be recall
def calculator():
    # TODO 3: Making user input
    print(icon)
    num1 = float(input("What's the first number:\t"))
    # TODO 5: Giving loop for the iteration
    still_counting = True
    while still_counting:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation:\t")
        num2 = float(input("What's the next number:\t"))
        # TODO 4: Calling function in dictionary to give the result
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Continue counting for {answer}? [Y/N]:\t").lower()
        if choice == 'n':
            still_counting = False
            calculator()
        else:
            num1 = answer
            still_counting = True


calculator()
