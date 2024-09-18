s=int(input("Enter st:"))
e=int (input("Enter end:"))
for i in range (s,e+1):
    for j in range (2,i):
        if(i%j==0):
            break
    else:
        print(i)