# a = input("Enter a list of hobbies (CSV):- ")
# b = input("Enter a list of hobbies (CSV):- ")
# a = a.split(',')
# b = b.split(',')
# a = [x.strip() for x in a]
# b = [x.strip() for x in b]
# a = set(a)
# b = set(b)
# print("Common Hobbies:- ", a&b)
# print("Unique to a:- ", a-(a&b))
# print("Unique to b:- ", b-(a&b))


# a = input("Enter a sentence:- ")
# a = a.split(' ')
# a = [x.lower() for x in a]
# a = set(a)
# print(a)


# a = {1,2,3}
# b = {3,4,5}
# print("Union:- ",a.union(b))
# print("Intersection:- ",a&b)
# print("Unique to a:- ", a-b)

#not handled 2,,,,,,
x = input("Enter CSV numbers:- ")
x = x.split(',')
x = [y.strip() for y in x]
s = {}
for i in x:
    s[i]=None
print(s.keys())


