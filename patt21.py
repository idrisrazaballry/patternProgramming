'''
*        *
**      **
***    ***
****  ****
**********
**********
****  ****
***    ***
**      **
*        *
'''
def print_butterfly(n):
    # Upper half of the butterfly
    for i in range(1, n + 1):
        # Left stars
        print("*" * i, end="")
        # Middle spaces
        print(" " * (2 * (n - i)), end="")
        # Right stars
        print("*" * i)
        
    # Lower half of the butterfly
    for i in range(n, 0, -1):
        # Left stars
        print("*" * i, end="")
        # Middle spaces
        print(" " * (2 * (n - i)), end="")
        # Right stars
        print("*" * i)

# Test the pattern
print_butterfly(5)
