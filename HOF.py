from functools import reduce
# numbers = [12, 5, 8, 3, 10, 7, 4]
# a=list(filter(lambda x:x%2==0,numbers))
# b=list(map(lambda x:x**2,a))
# c=sorted(b,reverse=True)
# print(c)
# d=reduce(lambda x,y:x+y,b)
# print(d)

# numbers= [2, 5, 8, 3, 10, 7, 4]
# x=reduce(lambda x,y:x+y,sorted(map(lambda x:x**2,filter(lambda x:x%2==0,numbers)),reverse=True))
# print(x)

# n=[-3, 4, 7, -2, 5, 8, -6]
# y=reduce(lambda x,y:x+y,sorted(map(lambda x:x*3,filter(lambda x:x>0,n))))
# print(y)

m=[2, 5, 8, 3, 10, 7, 4]
z=reduce(lambda x,y:x+y,sorted(filter(lambda x:x>50,map(lambda x:x**2,m)),reverse=True))
print(z)