import copy
l={1,2,3,4}
k=copy.deepcopy(l)
print(l)
print(k)
l.add(5)
print(l)
print(k)
a=[1,2,3,[4,5,6]]
b=copy.deepcopy(a)
print(a)
print(b)
a[3].append(7)
print(a)
print(b)
