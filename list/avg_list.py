print("Enter list number")
n=int(input()) 
l=[]
i=0
while i<n:
    l.append(int(input("Enter number:")))
    i=i+1

# l1=[23,2,3,4,5,6,12]
s=0
for e in l:
    s=s+e
x=len(l)
avg=s/x
print(avg)