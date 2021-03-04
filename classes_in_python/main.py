class User:
    # constuctor
    # self is the object
    def __init__(self, user_add):
        self.user_add = user_add
        print('when we create a new object')
    pass


user = User('bally')

user.id = 1
user.name = 'swag'
print(user.id, user.name, user.user_add)
