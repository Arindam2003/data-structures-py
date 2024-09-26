l=[1,2,3,2,13,4,0,-1,-2,-3,-4]
p=[]
np=[]
for e in l:
    if(e>0):
        p.append(e)
    else:
        np.append(e)
print("Positive Number is: ")
print(p)
print("Non Positive Number: ")
print(np)
