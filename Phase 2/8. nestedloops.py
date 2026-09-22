# n = int(input("Enter a number:- "))
# if n<0:
#     print("Enter a positive number")
# else: 
#     for i in range(n):
#         for j in range(0,i+1):
#             print("*",end="")
#         print()


# n = int(input("Enter a number:- "))
# if n<0:
#     print("Enter a positive number")
# else:
#     for i in range(n):
#         if i==0 or i==n-1:
#             for j in range(n):
#                 print("*",end="")
#             print()
#         else:
#             for j in range(n):
#                 if j==0 or j==n-1:
#                     print("*",end="")
#                 else:
#                     print(" ",end="")
#             print()


# for i in range(1,51):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz",end=" ")
#     elif i%3==0:
#         print("Fizz",end=" ")
#     elif i%5==0:
#         print("Buzz",end=" ")
#     print(i)


# row = int(input("Enter number of rows: "))
# col = int(input("Enter number of cols: "))

# if row<=0 or col<=0:
#     print("Enter only positive numbers")
# else: 
#     for r in range(1,1+row):
#         for c in range(1,1+col):
#             print(r*c,end="\t")
#         print()


# a = 29
# for i in range(5):
#     x = int(input("Enter a number: "))
#     if x>a:
#         print("Enter a smaller number")
#     elif x<a:
#         print("Enter a larger number")
#     else:
#         print("Congratulations for guessing")
#         break


