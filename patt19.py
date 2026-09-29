
'''
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
'''
def hollow_diamond(n):
    # Upper half
    for i in range(1, n + 1):
        # Print leading spaces
        print(" " * (n - i), end="")
        # Print stars and inner spaces
        for j in range(1, 2 * i):
            if j == 1 or j == (2 * i - 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()
        
    # Lower half
    for i in range(n - 1, 0, -1):
        # Print leading spaces
        print(" " * (n - i), end="")
        # Print stars and inner spaces
        for j in range(1, 2 * i):
            if j == 1 or j == (2 * i - 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Output for n = 5
hollow_diamond(5)
