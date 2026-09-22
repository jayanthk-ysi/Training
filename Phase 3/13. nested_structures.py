# l = [
#     {
#         "title": "a",
#         "author": "aa",
#         "year": 2024
#     },
#     {
#         "title": "b",
#         "author": "bb",
#         "year": 2011
#     },
#     {
#         "title": "c",
#         "author": "cc",
#         "year": 2009
#     },
#     {
#         "title": "d",
#         "author": "dd",
#         "year": 2008
#     }
# ]
# for i in l:
#     if i['year']>2010:
#         print(i)


# l = {
#     "a": ["aa","ab","ac"],
#     "b": ["ba","bb","bc"],
#     "c": ["ca","cb","cc"]
# }
# for i in l:
#     print(f"Department {i} has {len(l[i])} employees.")


# tup = [('a',4),('b',3),('c',2),('d',10),('e',15)]
# print(sorted(tup,reverse=True,key= lambda x: x[1]))
# print(tup)


# l = {
#     "a": {"email": "a@gmail.com","phone": "1234567"},
#     "b": {"email": "b@gmail.com","phone": "1234567"}
# }
# x = input("Enter a contact name:- ")
# if x in l.keys():
#     print(l[x])
# else:
#     print("Contact not exist")
# a = input("Enter a contact name:- ")
# b = input("Enter a mail id:- ")
# c = input("Enter a phone number:- ")
# l[a]={"email":b,"phone":c}
# print(l)