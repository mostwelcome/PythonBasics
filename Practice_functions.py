'''problem 1:  if both numbers are even return the lesser number , if not return the greater number '''

print('problem 1')


def lesser_of_two_numbers(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            return b
        return a
    else:
        if a > b:
            print(a)
            return a
        return b


print(lesser_of_two_numbers(2, 5))

'''problem 2 : a function takes two word string as a paramter and return true if both words begins with same letter '''

print('problem 2')


def animal_crackers(text):
    words = text.lower().split(' ')
    if words[0][0] == words[1][0]:
        return True
    else:
        return False


print(animal_crackers('ahis true'))


'''Problem 3 : Given two integers , return true if the sum of integers is 20 or if one of the integers is 20 . If not, return false '''

print('Problem 3')


def makes_twenty(a, b):
    return a+b == 20 or a == 20 or b == 20


print(makes_twenty(10, 10))
