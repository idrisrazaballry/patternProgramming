27)     P         
        y         
        s         
        p         
P y s p i d e r s 
        d         
        e         
        r         
        s 


# 27
s1='Pyspiders'
if len(s1)%2!=0:
    for row in range(len(s1)):
        for col in range(len(s1)):
            if col == len(s1) // 2:
                print(s1[row], end=" ")
            elif row == len(s1)// 2:
                print(s1[col], end=" ")
            else:
                print(" ", end=" ")
        print()
else:
    print("Give odd length string: ")
