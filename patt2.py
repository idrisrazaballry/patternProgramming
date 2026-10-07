'''
1 * * * * 
1 2 * * * 
1 2 3 * * 
1 2 3 4 * 
1 2 3 4 5 
'''

n=5
for row in range(n):
    for col in range(n):
        if row>=col:
            print(col+1, end=" ")
        else:
            print('*', end=" ")
    print()

print()
