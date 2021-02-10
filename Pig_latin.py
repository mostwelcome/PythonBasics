""" If word starts with a vowel , add 'ay' to end
if word does not starts with a vowel, put first letter at the end then add 'ay' 
word - ordway
apple - appleay
"""


def pig_latin(word):
    first_letter = word[0]

    # check if firstletter is voewl
    if first_letter in 'aeiou':
        pig_word = word+'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word


print(pig_latin('word'))
