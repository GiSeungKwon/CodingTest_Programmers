list_a = [1, 2, 3, 4, 5]
for i, item in enumerate(list_a):
    print(f"{i} {item}")
list_a.remove(1)

print()

for i, item in enumerate(list_a):
    print(f"{i} {item}")