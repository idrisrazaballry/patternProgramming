24)      1    25)    *        26) *       *
      2              *              *   *  
    3            * * * * *            *    
  4                  *              *   *  
5                    *            *       *


# 24
n=int(input("Enter :"))

for row in range(n):
    for col in range(n):
        if row + col == n-1:
            print(row+1, end=" ")
        else:
            print(" ", end=" ")
    print()
print()

# Both 25 and 26 only work for odd numbers
# 25
n=int(input("Enter :"))

for row in range(n):
    for col in range(n):
        if row == n//2 or col == n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()

# 26
n=int(input("Enter :"))

for row in range(n):
    for col in range(n):
        if row == col or row + col == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
