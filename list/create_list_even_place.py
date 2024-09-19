print("Enter number seperate by comma")
l=[int (e) for e in input().split(',')]
print(l)
l1=[]
i=1
for e in l:
    if i%2==0:
        l1.append(e)
    i=i+1
print(l1)