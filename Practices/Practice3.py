from itertools import product


def empowerment():
    power = int(input("Write the power: "))
    exponent = int(input("Write the exponent: "))
    result = power ** exponent
    return result


def numberInLetters():
    units = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
             10: "ten"}
    number = int(input("Write a number[1-10]: "))
    print(units[number])


def leap_year():
    year = int(input("Write year: "))
    if year % 4 == 0:
        return True


def readTwoNumbers():
    number1 = int(input("Write first number: "))
    number2 = int(input("Write second number: "))
    if number1 == number2:
        return True
    elif number1 != number2:
        return False


def palindrome():
    for i in range((999 * 999), (100 * 100), -1):
        if str(i) == str(i)[::-1]:
            print(i)
            break


def validateId(id):
    count = len(str(abs(id)))
    print("Total number of digits : ", count)
    if count == 11:
        print("Valid ID! ")
    else:
        print("Invalid ID! ")


def readList():
    text = input("Write a list separate by comma: ")
    list = text.split(",")
    return list
def multipleOfSixOfTwoNumbers(x , y):
  
    if y < x:
        print('The first number should be greater than the second')
    for i in range(x, y):
        if i%6==0:
            for r in range(1,14):
                result  = r * i
                if r == 13:
                    print("\n")
                    break
                print(i, " X ", r, " = ", result) 

multipleOfSixOfTwoNumbers(10, 50)
# print(empowerment())
# numberInLetters()
# print(leap_year())
# print(readTwoNumbers())
# print(palindrome())
# print(validateId(2230043731))
# print(readList())
