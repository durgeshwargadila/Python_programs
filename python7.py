def find_sum(*args):
    s=0
    for i in args:
        s+=i
    return s
print(find_sum(10,20,30,50))

def find_avg(*args):
    s=0
    c=0
    for i in args:
        s+=i
        c+=1
    return s/c
print(find_avg(10,20,30,50,40))

def find_largest(*args):
    largest=max(args)
    return largest
print((find_largest(10,20,30,10,40)))

def find_product(*args):
    p=1
    for i in args:
        p*=i
    return p
print(find_product(1,5,6,10))

def display_student(**args):
    return args
print(display_student(name='durgesh',course='py_29',age=21))

def create_profile(**args):
    return args
print(create_profile(name='durgesh',age=21,city='wgl',email='durgesh@gmail.com'))

def check_settings(**args):
    return args
print(check_settings(notifications='off',ringtone='on',theme='dark'))