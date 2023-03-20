str1 = "Python 2023"
str2 = "Python 2023"
str3 = str2

print(str1 == str2) # True
print(str2 == str3) # True


str1 = "Python 2023"
str2 = "Python 2023"
str3 = "Java 11"

print(type(str1), hex(id(str1))) # <class 'str'> 0x7f9f9e47c670
print(type(str2), hex(id(str2))) # <class 'str'> 0x7f9f9e47c670
print(type(str3), hex(id(str3))) # <class 'str'> 0x7f9f9e47c7f0

str1 = "Python 2023"
str2 = "Python 2023"
str3 = "Java 11"

print(str1 == str2) # True
print(str2 == str3) # False


str1 = "Python 2023"
str2 = "Python 2023"
str3 = "Java 11"

print(type(str1), hex(id(str1))) # <class 'str'> 0x7f9f9e47c670
print(type(str2), hex(id(str2))) # <class 'str'> 0x7f9f9e47c670
print(type(str3), hex(id(str3))) # <class 'str'> 0x7f9f9e47c7f0
