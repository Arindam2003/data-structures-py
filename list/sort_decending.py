print("Enter list number")
n=int(input()) 
l=[]
i=0
while i<n:
    l.append(int(input("Enter number")))
    i=i+1
l1=sorted(l)
l1[::-1]
print(l1)