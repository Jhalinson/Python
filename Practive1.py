# Escriba en pantalla el tipo de dato que retorna la expresión 4 < 2
print(4<2)
if(4<2):
    print()
else:
    print("Boolean")
# 2- Almacene en una variable el nombre de una persona y al final muestre en la consola el me nsaje:
# “Bienvenido [nombrePersona]”
name = input("Write your name: ")
print("Welcome: "+name)

# 3- Evalúe si un número es par o impar y muestre en la consola el mensaje.
number = int(input("Write a number: "))
if(number % 2 == 1):
    print("The odd number: "+ str(number))
else:
    print("The number is even: " +str(number))
    
# 4- Almacene dos números y evalúe si el primero es mayor que el segundo. El resultado debe verse
# en la consola.
number1 = int(input("Write one number: "))
number2 = int(input("Write number second: "))
if(number1>number2):
    print("Number one is greater than number two")
else:
    print("Number two is greater than number one")
# 5- Convierta dólares a pesos.
dolar= int(input("Dollar amount: "))
dominicanPeso = 58.80
result = float(dolar * dominicanPeso)
print("The amount in pesos: "+ str(result))

# 6- Convierta grados celsius a Fahrenheit
celsius = int(input("Celsius ℃: ->"))
fahrenheit = 32
weatherResult = (celsius * 9 / 5) + fahrenheit
print(str(weatherResult)+"°F")
# 7- Almacene cuatro notas 90,95,77, 92 y las promedie. Al final debe decir su calificación en letras
# A, B,C,D, E ó F.
grade1 = int(input("Write grade #1: "))
grade2 = int(input("Write grade #2: "))
grade3 = int(input("Write grade #3: "))
grade4 = int(input("Write grade #4: "))
average = float(grade1+grade2+grade3+grade4)
if(average>=90):
    print("Your Grade is: A")
elif(average<=89 & average >=80):
    print("Your Grade is: B")
elif(average<=79 &  average >=75):
    print("Your Grade is: C")
elif(average<=74 & average >=70):
    print("Your Grade is: D")
elif(average<=69 & average >= 65):
    print("Your Grade is: E")
elif(average<=64):
    print("Your Grade is: F")

# 8- Que almacene monto, cantidad de cuotas, y porcentaje de interés anual de un préstamo y
# calcule la cuota mensual. (Amortizar mediante el sistema francés)

amount = int(input())
amount_of_fees =int(input())
annual_interest_percentage =int(input())