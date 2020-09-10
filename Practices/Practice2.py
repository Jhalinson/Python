from array import *
import random
#
# from pip._vendor.distlib.compat import raw_input
#
# n = int(input("Write the number of elements: "))
# con = 1
# total = 0
# for i in range(n):
#     elements = int(input("Write the numbers: "))
#     total = total + elements
#     con += 1
#
# print("{} {}".format("Total sum of elements: ", total))
# print("{} {}".format("Number of elements: ", con))
from pip._vendor.distlib.compat import raw_input

menu = {'1': "Convertir grados a Celsius a Fahrenheit", '2': "Convertir dólar a pesos",
        '3': "Convertir metros a pies", '4': "Salir"}

while True:
    options = menu.keys()
    for entry in options:
        print(entry, menu[entry])
        selection = raw_input("Please Select:")
    if selection == '1':
        print("add")
    elif selection == '2':
        print("delete")
    elif selection == '3':
        print("find")
    elif selection == '4':
        break
    else:
        print("Unknown Option Selected!")






