n=int(input("Enter number:"))
i=1
l=[]
while i<n:
    for e in range (2,2*n):
        for f in range(2,e):
            if(e%f==0):
                break;
        else:
            # print(e,end=" ")
            l.append(e)
        i=i+1
print(l)
