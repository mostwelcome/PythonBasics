# does python have  a block scope ?


# This is valid as this is inside if
names = ['swagata', 'Tua']
game_level = 3

if game_level == 3:
    new_turn = True

print(new_turn)

#This is not valid


# def my_turn():
#     if game_level == 3:
#         new_turn = True


# print(new_turn)

# print(new_turn)
# NameError: name 'new_turn' is not defined
