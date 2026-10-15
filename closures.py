# def electricity(rate_per_unit):
#     def units(no_of_units):
#         total=rate_per_unit*no_of_units
#         print(total)
#     return units
# a=electricity(3)
# a(400)
#
# def salary(bonus):
#     def bonus_salary(basic_salary):
#         total_salary=basic_salary+bonus
#         print(total_salary)
#     return bonus_salary
# b=salary(7000)
# b(10000)
#
# def discount(percent):
#     def product_price(price):
#         dis=price*percent
#         final_price=price-dis
#         print(final_price)
#     return product_price
# c=discount(0.3)
# c(1000)

# def bank_account(balance):
#     def withdraw(amount):
#         nonlocal balance
#         if amount>balance:
#             print("Insufficient funds")
#         else:
#             balance-=amount
#             print(balance)
#     return withdraw
# d=bank_account(10000)
# d(5000)
# d(12000)

# def movie(movie_name):
#     def person_name(name):
#         print(f"{name} likes watching {movie_name} movie")
#     return person_name
# e=movie("Bahubali")
# e("Durgesh")

# def multiplier(number1):
#     def multiply(number2):
#         print(number1*number2)
#     return multiply
# f=multiplier(10)
# f(3)

#
# def restaurant(food_item):
#     def quantity(qty):
#         print(f"{food_item} - {qty}")
#     return quantity
# g=restaurant("Biryani")
# g(4)

#
# def create_password(password):
#     def check_pass():
#         stored_pass="Durgesh2504"
#         if password==stored_pass:
#             print("Access Granted")
#         else:
#             print("Access Denied")
#     return check_pass
# h=create_password("Durgesh1234")
# h()

# def shopping_cart(item_name):
#     def inner(qty,price):
#         total_price=qty*price
#         print(item_name,qty,total_price,sep="  ")
#     return inner
# i=shopping_cart("RC-Car")
# i(3,1000)


# def counter():
#     count=0
#     def inner():
#         nonlocal count
#         count+=1
#         print(count)
#     return inner
# j=counter()
# j()
