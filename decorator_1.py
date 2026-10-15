# def add(x,y):
#     return x+y
# def sub(x,y):
#     return x-y
# def multiply(x,y):
#     return x*y
# def log_operation(func):
#     l = []
#     def inner(op,a,b):
#         nonlocal l
#         l.append((op.__name__))
#         print(f"performing {op.__name__} operation")
#         return func(op,a,b)
#     return inner
#
# @log_operation
# def operation(fun,a,b):
#     return fun(a,b)
#
# print(operation(add,2,3))
# print(operation(sub,10,5))

# def require_details(func):
#     def inner(username,email):
#         if username=="Durgesh" and email=="durgeshwargadila@gmail.com":
#             func(username,email)
#         else:
#             print(f"Invalid credentials:{username},{email}")
#     return inner
#
# @require_details
# def register_user(username,email):
#     print(f"Correct username:{username}")
#     print(f"Correct email:{email}")
# register_user(username="Durges",email="durgeshwargadia@gmail.com")

# def double_result(func):
#     def inner(a):
#         y=func(a)
#         return y*2
#     return inner
# @double_result
# def num(x):
#     return x
# print(num(5))
def limited_access(func):
    count = 0
    def inner(x,y):
        nonlocal count
        count+=1
        if count<=3:
            func(x,y)
        else:
            print("Limit exceeded")
    return inner
@limited_access
def attempt_login(username, password):
    print(f"username:{username}")
    print(f"password:{password}")
    print(f"Login Successful")
attempt_login("Durgesh","durgesh1234")
