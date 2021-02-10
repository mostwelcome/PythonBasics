print('problem 1')
''' takes a list and returns true if it contains 007 in order '''


def spy_game(li):
    code = [0, 0, 7, 'x']
    for i in li:
        if i == code[0]:
            code.pop(0)
    return len(code) == 1


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 7, 5]))
print(spy_game([1, 1, 2, 4, 0, 7, 5]))


print('Problem 2')
''' write a number returns number of prime numbers that exist up to and including a given number '''


def count_primes(num):
    flag = True
    sum = 0
    for i in range(2, num+1):
        for j in range(2, i):
            if i % j == 0:
                flag = False
        if flag == True:
            sum += 1
    return sum


print(count_primes(100))
