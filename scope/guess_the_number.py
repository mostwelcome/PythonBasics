from art import logo
import random
print(logo)

print('Welcome To The Number guessing game \nI am thinking a number betwwen 0 to 100')


actual_number = random.randint(0, 100)
print(actual_number)


def choose_level_modi():
    print('Please select a valid difficulty level')
    for i in range(2):
        level = input('Choose a difficulty . Type easy or hard -----  ')
        if level in diff:
            return diff[level]
    return diff['medium']


diff = {'hard': 5, 'easy': 10, 'medium': 7}
level = diff.get(
    input('Choose a difficulty . Type easy or hard -----  ').lower(), choose_level_modi)

no_of_attempt = level if isinstance(level, int) else level()
print(no_of_attempt)
while True:

    chosen_number = int(input('Guess a number'))
    if chosen_number == actual_number:
        print('yuuu huuu , u won')
        break
    elif abs(chosen_number-actual_number) == 1:
        print('Too close')
    elif chosen_number > actual_number:
        no_of_attempt -= 1
        print('Too high')
    elif chosen_number < actual_number:
        no_of_attempt -= 1
        print('Too low')

    if no_of_attempt == 0:
        print('You have lost all your attempts')
        break
