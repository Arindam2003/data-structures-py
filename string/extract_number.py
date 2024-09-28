s=str(input("Enter any:"))
l=[]
for e in s:
    if e.isdigit():
        l.append(int(e))
print(l)