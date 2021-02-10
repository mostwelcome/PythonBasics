
'''name of the function should be in lower base separated by _'''


"This is a default name name = 'Name' when we are not passing any parameter"


def name_of_function(name='Name'):
    '''should contain the description of the function'''
    print('Hello '+name)
    return name


result = name_of_function('swagata')
print(result)


def add(n1, n2):
    return n1+n2


result = add(20, 10)
print(result)
