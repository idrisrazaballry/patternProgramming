'''
      1 
    2   2 
  3       3 
4           4 
  3       3 
    2   2 
      1 
'''

n = 4
for i in list(range(1, n + 1)) + list(range(n - 1, 0, -1)):
    print("  " * (n - i), end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print(i, end=" ")
        else:
            print(" ", end=" ")
    print()
