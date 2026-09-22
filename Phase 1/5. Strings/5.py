# a = input("Enter a sentence:- ")
# print("First 5 characters:- ", a[:5])
# print("Last 5 characters:- ", a[-5:])
# print("Reversed sentence:- ", a[::-1])


# a = input("Enter a sentence:- ")
# b = "the"
# res = a.replace(b,"***")
# print(res)


# a = " pen , book ,bag"
# line_sep = a.replace(",","\n")
# line_sep = line_sep.replace(" ","")
# print("Separate Lines:- ", line_sep)
# arr_sep = a.replace(",","->")
# print("Arrow separator:- ", arr_sep)


# a = input("Enter a sentence:- ")
# print("Starts with capital:- ", (a>='A' and a<='Z'))
# print("Ends with fullstop:- ", a[-1]=='.')
# print("Count of 'e' in sentence:- ", a.count('e'))


x = input("Enter c for celcius to fahrenheit or f for the reverse:- ")
if x=='c':
    a = float(input("Enter the temperature in celcius:- "))
    fahreiheit = (a*(9/5))+32
    print(f"Temperature in fahrenheit: {fahreiheit:.2f}")
elif x=='f':
    a = float(input("Enter the temperature in fahrenheit:- "))
    celcius = ((a-32)*5)/9
    print(f"Temperature in fahrenheit: {celcius:.2f}")
else:
    print("Input either 'c' or 'f'")