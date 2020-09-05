#conditionals
# code blick is a set of instrutions that have relation
number = int(input())

if number % 2 == 0:
    print("Even number")
    
else:
    print("Odd number")
    
print("Write your age: ")
age = int(input())
if age >=18:
    print("you are of legal age")
else:
    print("you are a minor")