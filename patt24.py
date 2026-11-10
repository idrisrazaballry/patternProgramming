'''
4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 
'''
def concentric_pattern(n):
    size = 2 * n - 1
    for i in range(size):
        for j in range(size):
            # Calculate the distance to the closest border
            layer = min(i, j, size - 1 - i, size - 1 - j)
            # Print the value based on the layer depth
            print(n - layer, end=" ")
        print()

concentric_pattern(4)

