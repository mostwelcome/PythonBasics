'''problem 1: given a list , return true if array contains a 3 next to a 3 somehwere'''

print('problem 1')


def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False


print(has_33([2, 3, 4, 3, 0]))
print(has_33([1, 3, 3]))

print('problem 1 -- alternate way')


def has_33_another(nums):
    for i in range(0, len(nums)-1):
        if nums[i:i+2] == [3, 3]:
            return True
    return False


print(has_33([2, 3, 4, 3, 0]))
print(has_33([1, 3, 3]))


print('problem 2')

''' given a string , return a string where for every character in the origin there are three characters '''


def paper_doll(text):
    new = ""
    for i in text:
        new = new + i*3
    return new


print(paper_doll('Hello'))
print(paper_doll('Mississippi'))


print('Problem 3')

''' BlackJack : given three integers between 1 to 11 ,if the sum is < = 21 return their sum . If the sum exceeds 21 and
there's an eleven , reduce the total sum by 10 . Finally if the sum exceeds 21 , return 'BUST' '''


def blackjack(a, b, c):
    if sum([a, b, c]) <= 21:
        return sum([a, b, c])
    elif(11 in [a, b, c]):
        return sum([a, b, c])-10
    else:
        return 'BUST'


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))

print('problem 4')
''' return the sum of the numbers in the array , except ignore sections of numbers starting with a 6 and extending to the
next 9 . Return 0 for no numbers '''


def summer_69(arr):
    sum = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                sum += num
                break
            else:
                add = False

        while not add:
            if num != 9:
                break
            else:
                add = True
    return sum


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
