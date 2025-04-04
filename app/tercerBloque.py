#1 - Escribe un programa que solicite dos números enteros e imprima todos los números enteros entre ellos.
num1 = int(input("Primer número entero: "))
num2 = int(input("Segundo número entero: "))

inicio = min(num1, num2) + 1
fin = max(num1, num2)

for i in range(inicio, fin):
    print(i)
#2 - Escribe un programa para calcular cuántos días tomará que la colonia de una bacteria A supere o iguale a la colonia de una bacteria B, basado en tasas de crecimiento del 3% y 1.5%, respectivamente. Supón que la colonia A comienza con 4 elementos y B con 10.
a = 4  # Bacteria A
b = 10  # Bacteria B
dias = 0

while a < b:
    a *= 1.03  # Crecimiento 3%
    b *= 1.015  # Crecimiento 1.5%
    dias += 1

print(f"La bacteria A superará a B en {dias} días")
#3 - Para procesar una cantidad de 15 datos de evaluaciones de usuarios de un servicio de la empresa, necesitamos verificar si las calificaciones son válidas. Por lo tanto, escribe un programa que recibirá calificaciones del 0 al 5 y verificará si son valores válidos. Si se ingresa una calificación superior a 5 o inferior a 0, se repetirá hasta que el usuario ingrese un valor válido.
for _ in range(15):
    while True:
        calificacion = float(input("Ingrese calificación (0-5): "))
        if 0 <= calificacion <= 5:
            break
        print("¡Valor inválido! Intente nuevamente.")
    print("Calificación válida:", calificacion)
#4 - Desarrolla un programa que lea un conjunto indefinido de temperaturas en grados Celsius y calcule su promedio. La lectura debe detenerse al ingresar el valor -273°C.
temperaturas = []
while True:
    temp = float(input("Temperatura en °C (-273 para terminar): "))
    if temp == -273:
        break
    temperaturas.append(temp)

if temperaturas:
    promedio = sum(temperaturas) / len(temperaturas)
    print(f"Promedio: {promedio:.2f}°C")
else:
    print("No se ingresaron temperaturas válidas.")
#5 - Escribe un programa que calcule el factorial de un número entero proporcionado por el usuario. Recuerda que el factorial de un número entero es el producto de ese número por todos sus antecesores hasta llegar al número 1. Por ejemplo, el factorial de 5 es 5 x 4 x 3 x 2 x 1 = 120.
#Momento de los proyectos
numero = int(input("Número para calcular factorial: "))
factorial = 1

for i in range(1, numero + 1):
    factorial *= i

print(f"Factorial de {numero}: {factorial}")
#6 - Escribe un programa que genere la tabla de multiplicar de un número entero del 1 al 10, según la elección del usuario. Como ejemplo, para el número 2, la tabla de multiplicar debe mostrarse en el siguiente formato:
#Tabla de multiplicar del 2:
#2 x 1 = 2
#2 x 2 = 4
#[...]
#2 x 10 = 20
#Copia el código
numero = int(input("Número para tabla de multiplicar (1-10): "))
print(f"Tabla de multiplicar del {numero}:")

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
#7 - Los números primos tienen diversas aplicaciones en Ciencia de Datos, como en criptografía y seguridad. Un número primo es aquel que es divisible solo por sí mismo y por 1. Por lo tanto, crea un programa que solicite un número entero y determine si es un número primo o no.
numero = int(input("Número a verificar: "))
es_primo = True

if numero <= 1:
    es_primo = False
else:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

print(f"{numero} {'es' if es_primo else 'no es'} primo")
#8 - Vamos a comprender la distribución de edades de los pensionistas de una empresa de seguros. Escribe un programa que lea las edades de una cantidad no informada de clientes y muestre la distribución en los intervalos [0-25], [26-50], [51-75] y [76-100]. La entrada de datos se detendrá al ingresar un número negativo.
intervalos = {
    "[0-25]": 0,
    "[26-50]": 0,
    "[51-75]": 0,
    "[76-100]": 0
}

while True:
    edad = int(input("Edad (negativo para terminar): "))
    if edad < 0:
        break
    
    if 0 <= edad <= 25:
        intervalos["[0-25]"] += 1
    elif 26 <= edad <= 50:
        intervalos["[26-50]"] += 1
    elif 51 <= edad <= 75:
        intervalos["[51-75]"] += 1
    elif 76 <= edad <= 100:
        intervalos["[76-100]"] += 1

print("\nDistribución de edades:")
for intervalo, cantidad in intervalos.items():
    print(f"{intervalo}: {cantidad} personas")
#9 - En una elección para la gerencia de una empresa con 20 empleados, hay cuatro candidatos. Escribe un programa que calcule al ganador de la elección. La votación se realizó de la siguiente manera:
#Cada empleado votó por uno de los cuatro candidatos (representados por los números 1, 2, 3 y 4).
#También se contaron los votos nulos (representados por el número 5) y los votos en blanco (representados por el número 6).
#Al final de la votación, el programa debe mostrar el número total de votos para cada candidato, los votos nulos y los votos en blanco. Además, debe calcular y mostrar el porcentaje de votos nulos con respecto al total de votos y el porcentaje de votos en blanco con respecto al total de votos.
votos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for _ in range(20):
    while True:
        voto = int(input("Voto (1-4 candidatos, 5 nulo, 6 blanco): "))
        if 1 <= voto <= 6:
            break
        print("Voto inválido!")
    votos[voto] += 1

total_votos = sum(votos.values())

print("\nResultados:")
for candidato, cantidad in votos.items():
    if candidato <= 4:
        print(f"Candidato {candidato}: {cantidad} votos")
    elif candidato == 5:
        porcentaje = (cantidad / total_votos) * 100
        print(f"Votos nulos: {cantidad} ({porcentaje:.1f}%)")
    else:
        porcentaje = (cantidad / total_votos) * 100
        print(f"Votos en blanco: {cantidad} ({porcentaje:.1f}%)")

ganador = max(votos.items(), key=lambda x: x[1] if x[0] <= 4 else -1)
print(f"\nGanador: Candidato {ganador[0]} con {ganador[1]} votos")