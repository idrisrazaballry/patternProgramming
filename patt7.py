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

# 9
for row in range(5):
    for col in range(5):
        if row>=col:
            print("*", end=" ")
    print()
print()

# without if condition
for row in range(5):
    for col in range(row+1):
        print('*', end=" ")
    print()
print()

# 10
n=5
for row in range(1, n+1):
    for col in range(1, n+1):
        if row>=col:
            print(col, end=" ")
    print()
print()
