# def count_calls(func):
#     count=0
#     def inner():
#         nonlocal count
#         count+=1
#         print(f"You called {count} times...")
#         s=func()
#         return s
#     return inner
# @count_calls
# def gen_ticket():
#     return 100
# print(gen_ticket())
# print(gen_ticket())
# print(gen_ticket())
# print(gen_ticket())
# print(gen_ticket())



role=["manager","admin"]
def check_access(func):
    def inner(us,r):
        if r in role:
            func(us,r)
        else:
            print("access denied")
    return inner
@check_access
def view_report(username,role):
    print(f"username:{username}")
    print(f"role:{role}")
view_report("durgesh","manager")
view_report("vamshi","client")

