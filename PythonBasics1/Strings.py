str = "RahulShettyAcademy.com"
str1 = "Consulting firm"
str2 = "RahulShetty"
str3 = "  great "
print(str[1])# prints a
print(str[0:5])# prints Rahul, substring 0th to 4th element
print(str+str1)# Concatenation, prints RahulShettyAcademy.comConsulting firm
print(str2 in str)# Verify str2 is present in str, and return True
print(str1 in str)# Verify str1 is present in str, and return False
var = str.split(".")# splits the String in 2 based on .
print(var)# prints ['RahulShettyAcademy', 'com']
print(var[0])#prints RahulShettyAcademy
print(str3.strip())# strip removes begining and ending spaces of a string
print(str3.lstrip())# strip removes begining spaces of a string
print(str3.rstrip())# strip removes ending spaces of a string

print("Welcome....")
print("Welcome.... Develop")
print("Welcome.... Develop")
print("Welcome.... Develop")
