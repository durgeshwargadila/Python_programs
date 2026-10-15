a=int(input())
b=int(input())
s=0
fc=0
count=0
for i in range(a,b+1):
    c=0
    for j in range(2,(i//2)+1):
        if i%j==0:
            c+=1
    if c==0 and i!=1:
        fc+=1
        if fc%2==1:
            count+=1
            s+=i
print(s/count)


