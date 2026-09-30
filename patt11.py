'''
20) * * * * *    21) *          22) *              23) reverse of 22
    *       *        * *              *
    *       *        *   *              *
    *       *        *     *              *
    * * * * *        * * * * *              *

'''

# 20
n=int(input("Enter :"))

for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 21
n=int(input("Enter :"))

for row in range(n):
    for col in range(n):
        if row==n-1 or col==0 or row==col:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 22
n=int(input("Enter :"))

for row in range(n):
    for col in range(n):
        if row==col:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()

# 23
n=int(input("Enter :"))

for row in range(n):
    for col in range(n):
        if row + col == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
