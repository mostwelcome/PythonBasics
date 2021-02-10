'''problem 1: function that capitalizes first and fourth letter of a name '''

print('problem 1')


def old_macdonald(name):
    return name[:3].capitalize() + name[3:].capitalize()


print(old_macdonald('macdonald'))

print('problem 2')
''' problem 2: Given a sentence, return  a sentence with the words reversed '''


def master_yoda(text):
    l = text.split(' ')
    reversed = l[::-1]
    return ' '.join(reversed)


print(master_yoda('I am Home'))
print(master_yoda('We are Ready'))


print('Problem 3')
''' Given n , True if n is within 10 of either 100 or 200 '''


def almost_there(n):
    return (abs(100-n) <= 10 or (abs(200-n) <= 10))


print(almost_there(104))
print(almost_there(150))
