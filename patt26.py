'''
*********
 *     * 
  *   *  
   * *   
    *    
   * *   
  *   *  
 *     * 
*********
'''

n = 5
rows = 2 * n - 1

for i in range(rows):
    # Mirror the row index for the bottom half
    r = i if i < n else rows - 1 - i
    for j in range(2 * n - 1):
        if r == 0 or j == r or j == (2 * n - 2 - r):
            print("*", end="")
        else:
            print(" ", end="")
    print()
