# FizzBuzz

# Instructions
'''
You are going to write a program that automatically prints the solution to the FizzBuzz game.

> `Your program should print each number from 1 to 100 in turn.`

>   `When the number is divisible by 3 then instead of printing the number it should print "Fizz".`

>     `When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

>       `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`

e.g. it might start off like this:

```
`1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz`
```

`.... etc.`

# Hint

1. Remember your answer should start from 1 and go up to and including 100.

2. Each number/text should be printed on a separate line.

# Solution

[https://repl.it/@appbrewery/day-5-4-solution](https: // repl.it/@appbrewery/day-5-4-solution)

Alternatively: [https://en.wikipedia.org/wiki/Fizz_buzz](https: // en.wikipedia.org/wiki/Fizz_buzz)
'''
'''for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)'''

# map_ = dict()
# for i in range(3, 101, 3):
#     map_[i] = "Fizz"

# for i in range(5, 101, 5):
#     map_[i] = "Buzz"

# for i in range(15, 101, 15):
#     map_[i] = "FizzBuzz"

# for i in range(1, 101):
#     print(map_.get(i, i))

for i in range(1, 20):
    print((i % 3 == 0)*"Fizz"+(i % 5 == 0)*"Buzz" or i)
