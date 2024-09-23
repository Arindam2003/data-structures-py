n=int(input("Enter number:"))
i=1
while i<n:
    for e in range (2,2*n):
        for f in range(2,e):
            if(e%f==0):
                break;
        else:
            print(e,end=" ")
        i=i+1
