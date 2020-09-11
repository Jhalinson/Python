from array import *
from pip._vendor.distlib.compat import raw_input
import random


def randomNumbers():
    n = int(input("Write the number of elements: "))
    con = 1
    total = 0
    for i in range(n):
        elements = int(input("Write the numbers: "))
        total = total + elements
        con += 1
    print("{} {}".format("Total sum of elements: ", total))
    print("{} {}".format("Number of elements: ", con))


def convertDegreesCelsiusToFahrenheit():
    celsius = int(input("Celsius ℃: "))
    fahrenheit = 32
    weather_Result = (celsius * 9 / 5) + fahrenheit
    print(str(weather_Result) + "°F")
    mainMenu()


def convertMetersToFeet():
    meters = int(input("Enter the meters: "))
    feet = 3.281
    weather_Result = float(meters) * feet
    print(str(weather_Result) + "ft")
    mainMenu()


def convertDollarToPesos():
    dollar = int(input("Dollar amount: "))
    dominicanPeso = 58.80
    result = float(dollar * dominicanPeso)
    print("The amount in pesos: " + str(result))
    mainMenu()


def mainMenu():
    print("\n 1. Convertir grados a Celsius a Fahrenheit \n 2. Convertir dólar a pesos \n 3. Convertir metros a pies "
          "\n 4. Salir")
    selection = int(input("\nEnter your choice: "))

    if selection == 1:
        convertDegreesCelsiusToFahrenheit()
    elif selection == 2:
        convertDollarToPesos()
    elif selection == 3:
        convertMetersToFeet()
    elif selection == 4:
        exit()
    else:
        print("Unknown Option Selected!.   Enter 1-4")


def Multiply():
    for i in range(5, 1000, 5):
        for l in range(1, 13, 1):
            result = i * l
            print(i, "*", l, "=", result)


def AFP():
    return 0.0287 * 12


def SFS():
    return 0.0304 * 12


def annualSalary(salary):
    annual_salary = salary * 12
    print("Annual Salary: ", "RD$", annual_salary)
    return float(annual_salary)


def ISFCaculator():
    salary = float(input("Enter your salary: "))
    top_one = 416220
    top_two = 624329
    top_three = 867123
    isr = 0.00
    annual = annualSalary(salary)

    if annual <= top_one:
        isr = float(annual * AFP() * SFS())
    elif annual <= top_two:
        surplus = annual - top_one
        isr = float(surplus * 0.15 * AFP() * SFS())
    elif annual <= top_three:
        surplus = annual - top_two
        isr = float(312116 + (surplus * 0.15 * AFP() * SFS()))
    else:
        surplus = annual - top_three
        isr = float(79776 + (surplus * 0.25 * AFP() * SFS()))
    print("Your ISR: ", "RD$", int(isr / 12))


def cashMachine():
    print("Select bank: \n 1. ABC \n 2. other")
    bank = int(input())
    if bank == 1:
        cash_money = int(input("Enter the amount ro retire: "))
        bills = [1000, 500, 100]
        for i in range(len(bills)):
            b = cash_money / bills[i]
            if cash_money > 10000:
                print("Your limit: RD$10000")
                break
            elif b > 0:
                print(int(b), "bills", bills[i], "Dominican Pesos")
                cash_money %= bills[i]
    if bank == 2:
        print("This bank is not available")


randomNumbers()
mainMenu()
Multiply()
ISFCaculator()
cashMachine()
