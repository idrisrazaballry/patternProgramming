'''
     1 
    1 1 
   1 2 1 
  1 3 3 1 
 1 4 6 4 1 
'''

def pascals_triangle(n):
    for i in range(n):
        # Print leading spaces for alignment
        print(" " * (n - i), end="")
        
        # Compute binomial coefficient
        val = 1
        for j in range(i + 1):
            print(f"{val} ", end="")
            val = val * (i - j) // (j + 1)
        print()

pascals_triangle(5)

