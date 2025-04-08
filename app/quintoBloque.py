#1 - Escribe un código para instalar la versión 3.7.1 de la biblioteca matplotlib.
# Ejecutar en la terminal/consola, no es un script de Python
# pip install matplotlib==3.7.1
#2 - Escribe un código para importar la biblioteca numpy con el alias np.
import numpy as np
print("Numpy importado correctamente como np")
#3 - Crea un programa que lea la siguiente lista de números y elija uno al azar.
import random

#lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
numero_aleatorio = random.choice(lista)
print(f"Número seleccionado: {numero_aleatorio}")
#4 - Crea un programa que genere aleatoriamente un número entero menor que 100.
import random
numero = random.randint(0, 99)
print(f"Número aleatorio: {numero}")
#5 - Crea un programa que solicite a la persona usuaria ingresar dos números enteros y calcule la potencia del primer número elevado al segundo.
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
resultado = base ** exponente
print(f"{base}^{exponente} = {resultado}")
#Aplicando a proyectos

#6 - Se debe escribir un programa para sortear a un seguidor de una red social para ganar un premio. La lista de participantes está numerada y debemos elegir aleatoriamente un número según la cantidad de participantes. Pide a la persona usuaria que proporcione el número de participantes del sorteo y devuelve el número sorteado.
import random
participantes = int(input("Número de participantes: "))
ganador = random.randint(1, participantes)
print(f"¡El ganador es el número {ganador}!")
#7 - Has recibido una solicitud para generar números de token para acceder a la aplicación de una empresa. El token debe ser par y variar de 1000 a 9998. Escribe un código que solicite el nombre de la persona usuaria y muestre un mensaje junto a este token generado aleatoriamente.

#print(f"Hola, {nombre_usuario}, tu token de acceso es {token_generado} ¡Bienvenido/a!")
import random
nombre_usuario = input("Ingrese su nombre: ")
token_generado = random.randrange(1000, 9999, 2)  # Números pares entre 1000 y 9998
print(f"Hola, {nombre_usuario}, tu token de acceso es {token_generado} ¡Bienvenido/a!")
#8 - Para diversificar y atraer nuevos clientes, una lanchonete creó un ítem misterioso en su menú llamado "ensalada de frutas sorpresa". En este ítem, se eligen aleatoriamente 3 frutas de una lista de 12 para componer la ensalada de frutas del cliente. Crea el código que realice esta selección aleatoria según la lista dada.

#frutas = ["manzana", "banana", "uva", "pera", "mango", "coco", "sandia", "fresa", "naranja", "maracuya", "kiwi", "cereza"]
import random
frutas = ["manzana", "banana", "uva", "pera", "mango", "coco", 
          "sandia", "fresa", "naranja", "maracuya", "kiwi", "cereza"]
ensalada = random.sample(frutas, 3)
print("Tu ensalada contiene:", ", ".join(ensalada))
#9 - Has recibido un desafío para calcular la raíz cuadrada de una lista de números, identificando cuáles resultan en un número entero. La lista es la siguiente:

#numeros = [2, 8, 15, 23, 91, 112, 256]
import math
numeros = [2, 8, 15, 23, 91, 112, 256]

for num in numeros:
    raiz = math.sqrt(num)
    if raiz.is_integer():
        print(f"√{num} = {int(raiz)} (entero)")
    else:
        print(f"√{num} = {raiz:.2f}")
#10 - Haz un programa para una tienda que vende césped para jardines. Esta tienda trabaja con jardines circulares y el precio del metro cuadrado de césped es de R$ 25,00. Pide a la persona usuaria el radio del área circular y devuelve el valor en reales de cuánto tendrá que pagar.
import math
radio = float(input("Ingrese el radio del jardín circular (metros): "))
area = math.pi * (radio ** 2)
costo = area * 25
print(f"Costo total del césped: R$ {costo:.2f}")