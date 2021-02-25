global_scope = 1


def increase_global():
    global global_scope
    global_scope += 1


print(increase_global())
print(global_scope)
