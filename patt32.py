'''
        * * * * * 
      *       * * 
    *       *   * 
  *       *     * 
* * * * *       * 
*       *     *   
*       *   *     
*       * *       
* * * * *         
'''

n = 5
size = 2 * n - 1

for i in range(size):
    for j in range(size):
        # Top face, front face, and connecting depth edges
        top_edge = (i == 0 and j >= n - 1) or (i == n - 1 and j < n)
        bottom_edge = (i == size - 1 and j < n)
        verticals = (j == 0 and i >= n - 1) or (j == n - 1 and i >= n - 1) or (j == size - 1 and i < n)
        diagonals = (i + j == n - 1) or (i + j == 2 * n - 2 and i < n) or (i + j == 3 * n - 3)
        
        if top_edge or bottom_edge or verticals or diagonals:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
