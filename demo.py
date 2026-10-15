n=int(input())
for i in range(1,n+1):
    a,p,c=i,2,0
    for j in range(1,i+1):
        while c<a:
            for k in range(2,p):
                if p%k==0:
                    break
            else:
                c+=1
                if c==a:
                    print(p,end=" ")
            p+=1
        a+=n-j
    print()

