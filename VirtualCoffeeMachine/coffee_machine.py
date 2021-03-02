from resource import resources
from resource import MENU
from resource import profit
is_on = True


def calculate_profit():
    '''Calculates the total profit '''
    print('Please insert coins')
    total = int(input('How many quarters ? ')) * 0.25
    total += int(input('How many dimes ? ')) * 0.1
    total += int(input('How many nickels ? ')) * 0.05
    total += int(input('How many pennies ? ')) * 0.01
    return total


def check_resource_available(ingredients_dict):
    ''' returns true if resource is available otherwise returns false '''
    for i in ingredients_dict:
        if (resources.get(i) < ingredients_dict.get(i)):
            print(f'Sorry there is not enought {i}')
            return False
    return True


def is_transaction_sucessful(money_received, cost_of_drink):
    ''' returns true if transaction is sucessfull , otherwise returnss false '''
    if money_received >= cost_of_drink:
        global profit
        profit += cost_of_drink
        change = round(money_received - cost_of_drink, 2)
        print(f'Here is the change {change}')
        return True
    else:
        print('Sorry that is not enough money. Money is refunded')
        return False


def make_coffe(choice, ingredients_dict):
    for i in ingredients_dict:
        resources[i] -= ingredients_dict.get(i)
    print(f'Here is ur {choice} ️️. Enjoy')


while is_on:
    choice = input(
        'What would you like? (espresso/latte/cappuccino): ').lower()

    if choice == 'off':
        break
    elif choice == 'report':
        for i in resources:
            print(f'{i.title()}:{resources[i]}')
        print(f'Money: ${profit}')

    else:
        money_received = 0
        ingredients_dict = MENU.get(choice).get('ingredients')
        resource_availabe = check_resource_available(ingredients_dict)
        if resource_availabe:
            money_received = calculate_profit()
            if is_transaction_sucessful(
                    money_received, MENU.get(choice).get('cost')):
                make_coffe(choice, ingredients_dict)
            else:
                print('Sorry')
