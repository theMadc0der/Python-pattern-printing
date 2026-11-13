print("How many rows you want to print:")
n = int(input())
print("Type 1 or 0")
a = int(input())
new = bool(a)

if new == True:
    for i in range(1,  n + 1):
        for j in range(i):
            print("*", end="")
        print()
else:
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end="")
        print()

            