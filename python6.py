
def find_sum(*args):
    s = 0
    for i in args:
        s+=i
    print(s)
find_sum(10,20,30,10)

def f_s(*args):
    return sum(args)
print(f_s(2,3,4,5))