# def outer():
#     print("Outer function started")
#     def inner():
#         print("Inner function started")
#     return inner
# x=outer()
# x()
#
# def greeting():
#     print("Welcome")
#     def say_hello():
#         print("Hello,Student")
#     return say_hello
# a=greeting()
# a()

# def calculate(a):
#     def square(b):
#         print(a**b)
#     return square
# y=calculate(2)
# y(2)


# def operations(a,b):
#     def add():
#         print(a+b)
#     return add
# z=operations(10,20)
# z()

# def message():
#     def display(name):
#         print("hello",name,end="")
#     return display
# b=message()
# b("Durgesh")


# def calculator():
#     def add(a,b):
#         print(a+b)
#     def multiply(a,b):
#         print(a*b)
#     return add,multiply
# c,d=calculator()
# c(4,5)
# d(4,5)

#
# def outer():
#     message="hello"
#     def inner():
#         print(message)
#     return inner
#
# e=outer()
# e()

# def calculate():
#     def add(a,b):
#         return a+b
#     return add
# f=calculate()
# g=f(2,3)
# print(g)

# def  check_number(number):
#     def check():
#         if number%2==0:
#             print("Even")
#         else:
#             print("Odd")
#     return check
# v=check_number(4)
# v()

def student_details(name):
    def display():
        print(f"student_name:{name}")
    return display
w=student_details("durgesh")
w()