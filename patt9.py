'''
        * 
      * * 
    * * * 
  * * * * 
* * * * * 

        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 

'''

# 15
n=5
for row in range(1, n+1):
    # space loop
    for spc in range(n-row):
        print(" ", end=" ")
    
    # start loop
    for star in range(row):
        print("*", end=" ")
    print()
print()

# 16
n=5
for row in range(1, n+1):
    # space loop
    for spc in range(n-row):
        print(" ", end=" ")
    
    # start loop
    for star in range(row):
        print(star+1, end=" ")
    print()
print()
