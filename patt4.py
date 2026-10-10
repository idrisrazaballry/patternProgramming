
'''
1 2 3 4 5 
* * * * * 
1 2 3 4 5 
* * * * * 
1 2 3 4 5 
'''

n = 5
for row in range(1, n+1):
    for col in range(1, n+1):
        if row%2==0:
            print('*', end=" ")
        else:
            print(col, end=" ")
    print()
print()
