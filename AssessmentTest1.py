ST = 'Print only the words start with s in this statement'
l = ST.split(' ')
for word in l:
    if word.startswith('s'):
        print(word)


for i in range(0, 11):
    if i % 2 == 0:
        print(i)

print('1 to 50 all numbers divisible by 3')
for i in range(1, 51):
    if i % 3 == 0:
        print(i)
print('using list comprehension')
print([i for i in range(1, 51) if i % 3 == 0])

print('even lengh word')

ST = 'Print every word in this sentence that has an even number of letters'
words = ST.split(' ')
for w in words:
    if len(w) % 2 == 0:
        print(w)

print('using list comprehension')
print([w for w in words if len(w) % 2 == 0])

print('Classic FizzBuzz problem')

for i in range(0, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

print('Create a list of the first letters of every word in this string')
ST = 'Create a list of the first letters of every word in this string'
print([word[0] for word in ST.split(' ')])
