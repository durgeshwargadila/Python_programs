def greet(name):
    return name
welcome=greet
print(welcome('durgesh'))

def square(a):
    return a**2
s=square
print(s(7))

def message():
    print("Hello")
hi=message
hi()
hi()
hi()

count=len
l=[1,2,3,4]
print(count(l))

display=print
display("Functional References")

def cube(n):
    return n**3
def apply(a):
    return a
print(apply(cube(2)))

def calculator(a,b,operation):
    return operation(a,b)
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
print(calculator(1,2,add))

def check(value):
    if value:
        print("even")
    else:
        print("odd")
def is_even(num):
    if num%2==0:
        return True
    else:
        return False
check(is_even(2))