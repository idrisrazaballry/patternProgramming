'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''
n = 5

for i in range(1, n + 1):
    # Print spaces to center-align, then print odd number of stars
    print(" " * (n - i) + "* " * i)

