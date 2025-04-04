#1 - Crea un programa que solicite al usuario que escriba su nombre y luego imprima "Hola, [nombre]."
nombre = input("Escribe tu nombre: ")
print(f"Hola, {nombre}.")
#2 - Crea un programa que solicite al usuario que escriba su nombre y edad, y luego imprima "Hola, [nombre], tienes [edad] años."
nombre = input("Nombre: ")
edad = input("Edad: ")
print(f"Hola, {nombre}, tienes {edad} años.")
#3 - Crea un programa que solicite al usuario que escriba su nombre, edad y altura en metros, y luego imprima "Hola, [nombre], tienes [edad] años y mides [altura] metros."
nombre = input("Nombre: ")
edad = input("Edad: ")
altura = input("Altura (metros): ")
print(f"Hola, {nombre}, tienes {edad} años y mides {altura} metros.")
#Calculadora con operadores
#4 - Crea un programa que solicite dos valores numéricos al usuario y luego imprima la suma de ambos valores.
a = float(input("Primer número: "))
b = float(input("Segundo número: "))
print(a + b)
#5 - Crea un programa que solicite tres valores numéricos al usuario y luego imprima la suma de los tres valores.
a = float(input("Número 1: "))
b = float(input("Número 2: "))
c = float(input("Número 3: "))
print(a + b + c)
#6 - Crea un programa que solicite dos valores numéricos al usuario y luego imprima la resta del primero menos el segundo valor.
a = float(input("Minuendo: "))
b = float(input("Sustraendo: "))
print(a - b)
#7 - Crea un programa que solicite dos valores numéricos al usuario y luego imprima la multiplicación de los dos valores.
a = float(input("Primer número: "))
b = float(input("Segundo número: "))
print(a * b)
#8 - Crea un programa que solicite dos valores numéricos, un numerador y un denominador, y realice la división entre los dos valores. Asegúrate de que el valor del denominador no sea igual a 0.
numerador = float(input("Numerador: "))
denominador = float(input("Denominador: "))
if denominador == 0:
    print("Error: Denominador no puede ser 0.")
else:
    print(numerador / denominador)
#9 - Crea un programa que solicite dos valores numéricos, un operador y una potencia, y realice la exponenciación entre estos dos valores.
base = float(input("Base: "))
exponente = float(input("Exponente: "))
print(base ** exponente)
#10 - Crea un programa que solicite dos valores numéricos, un numerador y un denominador, y realice la división entera entre los dos valores. Asegúrate de que el valor del denominador no sea igual a 0.
numerador = int(input("Numerador: "))
denominador = int(input("Denominador: "))
if denominador == 0:
    print("Error: Denominador no puede ser 0.")
else:
    print(numerador // denominador)
#11 - Crea un programa que solicite dos valores numéricos, un numerador y un denominador, y devuelva el resto de la división entre los dos valores. Asegúrate de que el valor del denominador no sea igual a 0.
numerador = int(input("Numerador: "))
denominador = int(input("Denominador: "))
if denominador == 0:
    print("Error: Denominador no puede ser 0.")
else:
    print(numerador % denominador)
#12 - Crea un código que solicite las 3 notas de un estudiante e imprima el promedio de las notas.
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
print((n1 + n2 + n3) / 3)
#13 - Crea un código que calcule e imprima el promedio ponderado de los números 5, 12, 20 y 15 con pesos respectivamente iguales a 1, 2, 3 y 4.
notas = [5, 12, 20, 15]
pesos = [1, 2, 3, 4]
total = sum(n * p for n, p in zip(notas, pesos))
suma_pesos = sum(pesos)
print(total / suma_pesos)
#Editando textos
#14 - Crea una variable llamada "frase" y asígnale una cadena de texto de tu elección. Luego, imprime la frase en pantalla.
frase = "Python es genial"
print(frase)
#15 - Crea un código que solicite una frase y luego imprima la frase en pantalla.
frase = input("Escribe una frase: ")
print(frase)
#16 - Crea un código que solicite una frase al usuario y luego imprima la misma frase ingresada pero en mayúsculas.
frase = input("Frase: ")
print(frase.upper())
#17 - Crea un código que solicite una frase al usuario y luego imprima la misma frase ingresada pero en minúsculas.
frase = input("Frase: ")
print(frase.lower())
#18 - Crea una variable llamada "frase" y asígnale una cadena de texto de tu elección. Luego, imprime la frase sin espacios en blanco al principio y al final.
frase = "   Hola Mundo   "
print(frase.strip())
#19 - Crea un código que solicite una frase al usuario y luego imprima la misma frase sin espacios en blanco al principio y al final.
frase = input("Frase: ").strip()
print(frase)
#20 - Crea un código que solicite una frase al usuario y luego imprima la misma frase sin espacios en blanco al principio y al final, además de convertirla a minúsculas.
frase = input("Frase: ").strip().lower()
print(frase)
#21 - Crea un código que solicite una frase al usuario y luego imprima la misma frase con todas las vocales "e" reemplazadas por la letra "f".
frase = input("Frase: ")
print(frase.replace('e', 'f'))
#22 - Crea un código que solicite una frase al usuario y luego imprima la misma frase con todas las vocales "a" reemplazadas por el carácter "@".
frase = input("Frase: ")
print(frase.replace('a', '@'))
#23 - Crea un código que solicite una frase al usuario y luego imprima la misma frase con todas las consonantes "s" reemplazadas por el carácter "$".
frase = input("Frase: ")
print(frase.replace('s', '$'))