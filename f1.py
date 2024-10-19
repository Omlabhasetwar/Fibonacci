l=[]
n=int(input("Enter a no"))
for i in range(n):
    if(i==0 or i==1):
        l.append(i)
    else:
        l.append(l[-1] + l[-2])
print(l)