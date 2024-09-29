a = 34
b = 23.45
# print(a+b)
# print(type(b))

e = '31'
e = int(31)


name = "Meet"
# print(len(name))
# print(name[0:3:2])
var1 = name.lower()
var2 = name.upper()
var3 = name.replace("ee" , "i")

str1 = "This is a "
name1 = "Meet"
name2 = "Dhruv"
str2 = "This is not a"
temp = "This is a {} and he is a good boy named {}".format(name1,name2)
temp2 = f"This is a {name1} and he is a good boy {name2}"

x = 52
# print(x)
 
# 1. ** Exponential Operator(to find power of any number)
# 2. // Floor division operator(returns only int value of divison)
# 3. % Modulo operator(to find reminder of the two numbers)

''' 
Python Collections
1. List
2. Tuple
3. Set
4. Dictionary
'''
# 1.List
lst = [2,3,5,7,8,1]
var = type(lst)

# 2.Tuple
a = ("Meet", "Dhruv", "Nisit")
var = type(a)
# print(var)
# print(a)

# 3.Set
s1 = {23,45,3,3,3,3,46,6,7,2,3,5,7,7,6,6,6,}
# print(s1)

# 4.Dictionary
meetDict = {
    "Name": "Meet",
    "Class":"First",
    "CGPA":7.98
}
# print(meetDict)

# Conditional Formating
# age = input("Enter Your age: ")
# age = int(age)
# print(type(age))
# if(age>18):
#     print("You can drive a car")
# elif(age==18):
#     print("You are eligible for drive a car")
# else:
#     print("You can`t drive")

# # Loops
# for i in range(0,100):
#     print(i)


# while loop
# i = 0
# while(i<100):
#     i = i + 1
#     if i == 34:
#         continue
#     print(i+1)
    

# Functins:
# def fun1(a,b):
#     c = a + b
#     return c
# d = fun1(34,21)
# print(d)

class Employee:
    def __init__(self,gname,gsalary):
        self.name = gname
        self.salary = gsalary
    
Meet = Employee("Meet",20000)
# print(Meet.name)
# print(Meet.salary)


# To generate random numbers 
import random
r = random.randrange(-1,10)
print(r)