'''
       * 
      * * 
     *   * 
    * * * * 
   *       * 
  * *     * * 
 *   *   *   * 
* * * * * * * * 
'''
n = 8  # Works best with powers of 2 (4, 8, 16)

for y in range(n - 1, -1, -1):
    print(" " * y, end="")
    for x in range(n - y):
        if (x & y) == 0:
            print("* ", end="")
        else:
            print("  ", end="")
    print()

