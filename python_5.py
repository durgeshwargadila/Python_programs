def find_power(value,exp):
    print(value ** exp)
value=int(input())
exp=int(input())
find_power(value,exp)



def calculate_bill(units,price):
    total_bill=units * price
    return total_bill
units=int(input())
price=int(input())
total_bill=calculate_bill(units,price)
print(total_bill)


def check_login(username,password):
    if "@gmail.com" in username:
        if len(password)>=8:
            return "Login Successful"
        else:
            return "Invalid Credentials"
    else:
        return "Invalid Credentials"
username=input()
password=input()
print(check_login(username,password))


details={"charan":"python123",
         "john":"hello456",
         "emma":"pass789"}
def login(username,password):
    if username in details:
        if password == details[username]:
            return "True"
        else:
            return "False"
    else:
        return "False"
username=input()
password=input()
print(login(username, password))

def add_item(item,items=None):
    items=[]
    items.append(item)
    return items
print(add_item(10))
print(add_item(20))
print(add_item(30))




def add_student(name,students=None):
    students={}
    students[name]="present"
    return students
print(add_student("durgesh"))
print(add_student('vamshi'))
