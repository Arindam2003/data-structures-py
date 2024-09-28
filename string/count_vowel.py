x=input("Enter a String:")
v="aeiouAEIOU"
count=0
for e in x:
    if e in v:
        count=count+1

print(count)