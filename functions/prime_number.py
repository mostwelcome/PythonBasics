# Write your code below this line 👇
import math


def prime_checker(number):
    flag = False
    if number == 1:
        print('prime')
    for i in range(2, math.ceil(number/2)+1):
        if number % i == 0:
            flag = True
            break
    if flag == True:
        print('Not prime')
    else:
        print('prime')


# Write your code above this line 👆


# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
