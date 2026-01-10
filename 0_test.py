a = [1, 2, 3]
b = a
b[0] = 10
print(a, id(a))
print(b, id(b))

def change(param_list):
    param_list[0] = 100

change(a)
print(a, id(a))
print(b, id(b))