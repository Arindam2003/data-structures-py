s=input("Enter Semtence")   #Arindam dinda my name
x=s.split(" ")
max=0
for e in x:
    count=0
    for i in e:
        count=count+1
    if(count>max):
        max=count

for i in x:
    if len(i)==max:
        print(i)