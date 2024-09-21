n=int (input("Enter number:"))
l=[]
pre=-1
nxt=1
i=1
while i<=n:
    current=pre+nxt
    l.append(current)
    pre=nxt
    nxt=current
    i=i+1
print(l)