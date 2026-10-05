'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 

'''

n = 5

# 1. Top Half
for i in range(1, n + 1):
    # Print leading spaces
    print(" " * (n - i), end="")
    # Print stars with trailing spaces
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# 2. Bottom Half
for i in range(n - 1, 0, -1):
    # Print leading spaces
    print(" " * (n - i), end="")
    # Print stars with trailing spaces
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
