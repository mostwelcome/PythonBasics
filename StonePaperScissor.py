import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user = int(
    input('What do u choose ? Type 0 for rock , 1 for paper and 2 for Scissor . '))

if user == 0:
    print(rock)
elif user == 1:
    print(paper)
elif user == 2:
    print(scissors)

generated = random.randint(0, 2)
print('Computer')
if generated == 0:
    print(rock)
elif generated == 1:
    print(paper)
elif generated == 2:
    print(scissors)

if abs(user-generated) > 1:
    if user < generated:
        print('you won')
    else:
        print('I am the winner')
else:
    if user > generated:
        print('you won')
    elif generated > user:
        print('I am the winner')
    else:
        print('haha its a draw')
