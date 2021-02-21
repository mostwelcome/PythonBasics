# from replit import clear

from art import logo
# HINT: You can call clear() to clear the output in the console.
print(logo)


def check_for_more_ppl():
    more_ppl_flag = True
    more_ppl = input('want to add more ppl ? type yes or no  ')
    if more_ppl.lower() == 'no':
        more_ppl_flag = False
    elif more_ppl.lower() == 'yes':
        # way of cleaning screen when from replit import clear doesn't work
        print('\n')
        print("\x1B[2J")
    else:
        print('Invalid Input. Please try again')
        check_for_more_ppl()
    return more_ppl_flag


dict_bid = {}
while True:
    name = input('What is your name : ')
    bid = int(input('what is your bid? $'))
    dict_bid[name] = bid
    more_ppl_flag = check_for_more_ppl()
    if more_ppl_flag == False:
        break

print(dict_bid)

max_bid = max(dict_bid, key=dict_bid.get)
print(f'{max_bid} own with bid of ${dict_bid[max_bid]}')
