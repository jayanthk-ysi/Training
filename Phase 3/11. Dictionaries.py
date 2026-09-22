# x = input("Enter a word:- ")
# d = {}
# for i in x:
#     if i not in d.keys():
#         d[i] = x.count(i)
# print(d)


# d = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
#     "d": 4,
#     "e": 5
# }
# inp = input("Enter an item name:- ")
# if inp in d.keys():
#     print("Quantitiy is:- ",d[inp])
# else:
#     print("Item isn't in cart")


# inp = input("Enter a sentence:- ")
# inp = inp.split(' ')
# inp = [x.strip().lower() for x in inp]
# d = {}
# for i in inp:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)


#not handled integers
# d = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
#     "d": 4
# }
# inp = input("Enter a student name:- ")
# x = float(input("Enter their marks:- "))
# d[inp]=x
# d['c']=50.5
# print(d)



# d = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
#     "d": 4,
#     "e": 5
# }
# ct = {x:d[x] for x in d if d[x]>3}
# print(ct)


