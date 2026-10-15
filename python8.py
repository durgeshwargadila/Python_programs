def simple_interest(principle,rate=5,time=1):
     print((principle*time*rate)/100)
simple_interest(1000)
simple_interest(2500,time=2,rate=3)

def student_info(name,*subjects,**details):
    print(name,*subjects,details)
student_info('durgesh','maths','phy','chem',grade='A',school='SR High School')

def order_food(*items,**preferences):
    print(*items,preferences)
order_food('biryani','pasta','fried_rice',spice_level='medium',delevery_time='7:00 PM')

def shopping_cart(*prices,discount=0):
    total=0
    for i in prices:
        total+=i
    print(total-discount)
shopping_cart(100,200,300,400,discount=200)

def register_user(username,*permissions,role='user',**details):
    print(username,role,permissions,details)
register_user('durgesh','can take leave','can come late',user_age=21,fee_paid='yes',role='student')
