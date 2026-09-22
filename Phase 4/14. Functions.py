# def func(a):
#     return a==a[::-1]

# print(func("aba"))
# print(func("abc"))
# print(func("abcdcba"))


# def func(a,b=0):
#     if(b<0):
#         print("Enter valid discount")
#         return None
#     elif a<0:
#         print("Enter a valid amount")
#         return None
#     else:
#         return a - (a*(b/100))

# print(func(100,50))
# print(func(10,-1))
# print(func(10))


# def func(*args):
#     return sum(args)/len(args)

# print(func(1,2,3))
# print(func(1,2,3,4,5,6))


# def func(**kwargs):
#     s=""
#     for a,b in kwargs.items():
#         s+=f"{a} is {b} "
#     return s
# print(func(name = "a",age = 10))
# print(func(age = 10,name = "a"))


# def func(l):
#     e=0
#     o=0
#     for i in l:
#         if i%2==0:
#             e+=1
#         else:
#             o+=1
#     return e,o
# e,o = func([1,2,3,4])
# print(e,o)


