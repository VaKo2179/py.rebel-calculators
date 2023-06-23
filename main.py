from os import system, name

def clear_console():
    print('\n' * 100)

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def add(n1, n2):
    return n1 + n2

def mult(n1, n2, n3):
    return n1 * n2

def sub(n1, n2):
    return n1 - n2

def div(n1, n2):
    return n1 / n2

operations = {"+": add, "*": mult, "-": sub, "/": div}

def calculation():
    num1 = int(input("Enter the first number: "))
    continue_operation = True

    while continue_operation:
        for oper in operations:
            print(oper)

        choose_operation = input("Choose an operator: ")
        if choose_operation not in operations:
            print("Invalid operator!")
            continue

        num2 = int(input("Enter the next number: "))

        operation = operations[choose_operation]
        result = operation(num1, num2)
        print("Result:", result)

        cont = input("Do you want to continue? (yes/no): ")
        if cont.lower() == "yes":
            num1 = result
        else:
            clear_console()
            continue_operation = False
            calculation()
            clear_console()


calculation()
