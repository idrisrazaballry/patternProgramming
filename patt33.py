'''
               * 
              * * 
             *   * 
            * * * * 
           *       * 
          * *     * * 
         *   *   *   * 
        * * * * * * * * 
       *               * 
      * *             * * 
     *   *           *   * 
    * * * *         * * * * 
   *       *       *       * 
  * *     * *     * *     * * 
 *   *   *   *   *   *   *   * 
* * * * * * * * * * * * * * * * 
'''

n = 16  # Best with powers of 2 (8, 16, 32)

for y in range(n - 1, -1, -1):
    print(" " * y, end="")
    for x in range(n - y):
        if (x & y) == 0:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
