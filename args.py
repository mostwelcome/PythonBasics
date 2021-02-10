

def my_func(a, b):
    # returns 5% of the sum of a and b
    return sum((a, b)) * 0.05


print(my_func(10, 10))

''' when we don't know how many arguments it can be -- returns tuple'''


'''args can be of anyname '''


def func(*args):
    print(args)


func(2, 3, 4, 5, 6, 7)


def keyword_arguments(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {} '.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')


keyword_arguments(fruit='apple', veggie='lettuce')

keyword_arguments(veggie='lettuce')


'''both together '''


def both_together(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like to have {} {} '.format(args[0], kwargs['food']))


both_together(10, 20, 30, fruit='apple', food='chicken', animal='dog')
