st=int(input("Start:"))
end=int(input("End:"))
for e in range (st,end):
    for i in range (2,e):
        if (e%i==0):
            break
    else:
        print(e,end=' ')
