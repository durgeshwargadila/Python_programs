n1=int(input())
n2=int(input())
s=0
n=0
d=0
for i in range(n1+1,n2):
    rev=0
    t=i
    while i>0:
        rem=i%10
        rev=rev*10+rem
        i//=10
        if t==rev:
            n+=1
            if n%2==1:
                s+=t
                d+=1
print(s/d)




