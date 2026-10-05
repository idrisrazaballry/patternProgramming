'''
35)     
         *           
        * * 
      * * * *
    * * * * * *

'''
# # 35
# n = int(input("Enter :"))
# spc = n - 1
# star = 1


# for row in range(n):
#     # space
#     for i in range(spc):
#         print(" ", end=" ")
    
#     # star
#     for i in range(star):
#         print("*", end=" ")
    
#     spc -= 1
#     star +=2
#     print()

# optimised one (without spc and star variable)
n=int(input("Enter :"))

for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end=" ")
    
    for k in range(1, i*2):
        # print("*", end=" ")
        # print(i, end=" ")
        print(k, end=" ")
    print()
