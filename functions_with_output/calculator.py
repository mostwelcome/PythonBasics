from art import logo

print(logo)


def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def multiply(a, b):
    return a*b


def div(a, b):
    return a/b


operation = ['+', '-', '*', '/']
result = 0
count = 0
while True:
    if count == 0:
        first_number = int(input('Enter first number'))
    else:
        first_number = result
    print(operation)
    which_operation = input('what you want to do?')
    second_number = int(input('Enter second number'))
    if which_operation == '+':
        result = add(first_number, second_number)
    elif which_operation == '-':
        result = sub(first_number, second_number)
    elif which_operation == '*':
        result = multiply(first_number, second_number)
    elif which_operation == '/':
        result = div(first_number, second_number)

    if_continue = input(
        'you want to continue ? store the result or continue ? type yes or no')
    if if_continue == 'no':
        print(f'Your result is : ----{result}')
        break
    else:
        count += 1
