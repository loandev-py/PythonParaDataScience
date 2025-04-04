#1 - Crea un programa que tenga la siguiente lista con los gastos de una empresa de papel [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]. Con estos valores, crea un programa que calcule el promedio de gastos. Sugerencia: usa las funciones integradas sum() y len().
gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
promedio = sum(gastos) / len(gastos)
print(f"Promedio de gastos: R$ {promedio:.2f}")
#2 - Con los mismos datos de la pregunta anterior, determina cuántas compras se realizaron por encima de 3000 reales y calcula el porcentaje con respecto al total de compras.
gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
compras_altas = sum(1 for gasto in gastos if gasto > 3000)
porcentaje = (compras_altas / len(gastos)) * 100
print(f"Compras > R$3000: {compras_altas} ({porcentaje:.1f}%)")
#3 - Crea un código que recoja en una lista 5 números enteros aleatorios e imprima la lista. Ejemplo: [1, 4, 7, 2, 4].
import random
numeros = [random.randint(1, 10) for _ in range(5)]
print("Lista aleatoria:", numeros)
#4 - Recoge nuevamente 5 números enteros e imprime la lista en orden inverso al enviado.
numeros = [int(input(f"Número {i+1}: ")) for i in range(5)]
print("Lista invertida:", numeros[::-1])
#5 - Crea un programa que, al ingresar un número cualquiera, genere una lista que contenga todos los números primos entre 1 y el número ingresado.
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

numero = int(input("Ingrese un número: "))
primos = [n for n in range(1, numero+1) if es_primo(n)]
print("Números primos:", primos)
#6 - Escribe un programa que pida una fecha, especificando el día, mes y año, y determine si es válida para su análisis.
dia = int(input("Día: "))
mes = int(input("Mes: "))
año = int(input("Año: "))

valido = True
if mes < 1 or mes > 12:
    valido = False
elif mes in [4,6,9,11] and dia > 30:
    valido = False
elif mes == 2:
    if (año % 400 == 0) or (año % 100 != 0 and año % 4 == 0):
        if dia > 29: valido = False
    elif dia > 28: valido = False
elif dia > 31:
    valido = False

print("Fecha válida" if valido else "Fecha inválida")
#Momento para los proyectos

#7 - Para un estudio sobre la multiplicación de bacterias en una colonia, se recopiló el número de bacterias multiplicadas por día y se puede observar a continuación: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Con estos valores, crea un código que genere una lista que contenga el porcentaje de crecimiento de bacterias por día, comparando el número de bacterias en cada día con el número de bacterias del día anterior. Sugerencia: para calcular el porcentaje de crecimiento, utiliza la siguiente ecuación: 100 * (muestra_actual - muestra_anterior) / muestra_anterior.
bacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
crecimiento = [100 * (bacterias[i]-bacterias[i-1])/bacterias[i-1] for i in range(1, len(bacterias))]
print("Porcentajes de crecimiento:", crecimiento)
#8 - Para una selección de productos alimenticios, debemos separar el conjunto de IDs proporcionados por números enteros, sabiendo que los productos con ID par son dulces y los que tienen ID impar son amargos. Crea un código que recoja 10 IDs. Luego, calcula y muestra la cantidad de productos dulces y amargos.
ids = [int(input(f"ID producto {i+1}: ")) for i in range(10)]
dulces = sum(1 for id in ids if id % 2 == 0)
amargos = len(ids) - dulces
print(f"Dulces: {dulces}, Amargos: {amargos}")
#9 - Desarrolla un programa que informe la puntuación de un estudiante de acuerdo con sus respuestas. Debe pedir la respuesta del estudiante para cada pregunta y verificar si la respuesta coincide con el resultado. Cada pregunta vale un punto y hay opciones A, B, C o D.

#Resultado del examen:
#01 - D
#02 - A
#03 - C
#04 - B
#05 - A
#06 - D
#07 - C
#08 - C
#09 - A
#10 - B
#Copia el código
respuestas = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']
puntos = 0

for i in range(10):
    respuesta = input(f"Respuesta pregunta {i+1} (A-D): ").upper()
    if respuesta == respuestas[i]:
        puntos += 1

print(f"Puntuación: {puntos}/10")
#10 - Un instituto de meteorología desea realizar un estudio de la temperatura media de cada mes del año. Para ello, debes crear un código que recoja y almacene esas temperaturas medias en una lista. Luego, calcula el promedio anual de las temperaturas y muestra todas las temperaturas por encima del promedio anual y en qué mes ocurrieron, mostrando los meses por su nombre (Enero, Febrero, etc.).
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
         'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
temps = [float(input(f"Temperatura {mes}: ")) for mes in meses]

promedio = sum(temps) / 12
print("\nTemperaturas sobre el promedio anual:")
for i in range(12):
    if temps[i] > promedio:
        print(f"{meses[i]}: {temps[i]:.1f}°C")
#11 - Una empresa de comercio electrónico está interesada en analizar las ventas de sus productos. Los datos de ventas se han almacenado en un diccionario:

#{'Producto A': 300, 'Producto B': 80, 'Producto C': 60, 'Producto D': 200, 'Producto E': 250, 'Producto F': 30}
#Copia el código
#Escribe un código que calcule el total de ventas y el producto más vendido.
ventas = {'Producto A': 300, 'Producto B': 80, 'Producto C': 60, 
          'Producto D': 200, 'Producto E': 250, 'Producto F': 30}

total = sum(ventas.values())
mas_vendido = max(ventas, key=ventas.get)
print(f"Total ventas: {total}")
print(f"Producto más vendido: {mas_vendido} ({ventas[mas_vendido]} unidades)")
#12 - Se realizó una encuesta de mercado para decidir cuál diseño de marca infantil es más atractivo para los niños. Los votos de la encuesta se pueden ver a continuación:

#Tabla de votos de la marca
#Diseño 1 - 1334 votos
#Diseño 2 - 982 votos
#Diseño 3 - 1751 votos
#Diseño 4 - 210 votos
#Diseño 5 - 1811 votos
#Copia el código
#Adapta los datos proporcionados a una estructura de diccionario. A partir de ello, informa el diseño ganador y el porcentaje de votos recibidos.
votos = {'Diseño 1': 1334, 'Diseño 2': 982, 'Diseño 3': 1751, 'Diseño 4': 210, 'Diseño 5': 1811}
total = sum(votos.values())
ganador = max(votos, key=votos.get)
porcentaje = (votos[ganador] / total) * 100

print(f"Ganador: {ganador} ({porcentaje:.1f}% de votos)")
#13 - Los empleados de un departamento de tu empresa recibirán una bonificación del 10% de su salario debido a un excelente rendimiento del equipo. El departamento de finanzas ha solicitado tu ayuda para verificar las consecuencias financieras de esta bonificación en los recursos. Se te ha enviado una lista con los salarios que recibirán la bonificación: [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]. La bonificación de cada empleado no puede ser inferior a 200. En el código, convierte cada uno de los salarios en claves de un diccionario y la bonificación de cada salario en el valor correspondiente. Luego, informa el gasto total en bonificaciones, cuántos empleados recibieron la bonificación mínima y cuál fue el valor más alto de la bonificación proporcionada.
salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
bonificaciones = {salario: max(salario * 0.1, 200) for salario in salarios}

total = sum(bonificaciones.values())
minimos = sum(1 for bono in bonificaciones.values() if bono == 200)
maximo = max(bonificaciones.values())

print(f"Gasto total en bonificaciones: R$ {total:.2f}")
print(f"Empleados con bono mínimo: {minimos}")
print(f"Bono más alto: R$ {maximo:.2f}")
#14 - Un equipo de científicos de datos está estudiando la diversidad biológica en un bosque. El equipo recopiló información sobre el número de especies de plantas y animales en cada área del bosque y almacenó estos datos en un diccionario. En él, la clave describe el área de los datos y los valores en las listas corresponden a las especies de plantas y animales en esas áreas, respectivamente.

#{'Área Norte': [2819, 7236], 'Área Leste': [1440, 9492], 'Área Sul': [5969, 7496], 'Área Oeste': [14446, 49688], 'Área Centro': [22558, 45148]}
#Copia el código
#Escribe un código para calcular el promedio de especies por área e identificar el área con la mayor diversidad biológica. Sugerencia: utiliza las funciones incorporadas sum() y len().
areas = {
    'Área Norte': [2819, 7236],
    'Área Leste': [1440, 9492],
    'Área Sul': [5969, 7496],
    'Área Oeste': [14446, 49688],
    'Área Centro': [22558, 45148]
}

promedios = {area: sum(especies)/len(especies) for area, especies in areas.items()}
mayor_diversidad = max(promedios, key=promedios.get)

print("Promedio de especies por área:")
for area, prom in promedios.items():
    print(f"{area}: {prom:.1f} especies")

print(f"\nÁrea con mayor diversidad: {mayor_diversidad}")
#15 - El departamento de Recursos Humanos de tu empresa te pidió ayuda para analizar las edades de los colaboradores de 4 sectores de la empresa. Para ello, te proporcionaron los siguientes datos:

#{'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
# 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
# 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
# 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
#Copia el código
#Dado que cada sector tiene 10 colaboradores, construye un código que calcule la media de edad de cada sector, la edad media general entre todos los sectores y cuántas personas están por encima de la edad media general.
sectores = {
    'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
    'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
    'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
    'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]
}

# Medias por sector
medias = {sector: sum(edades)/len(edades) for sector, edades in sectores.items()}

# Edad media general
todas_edades = [edad for edades in sectores.values() for edad in edades]
media_general = sum(todas_edades) / len(todas_edades)

# Personas sobre media general
sobre_media = sum(1 for edad in todas_edades if edad > media_general)

print("Media por sector:")
for sector, media in medias.items():
    print(f"{sector}: {media:.1f} años")

print(f"\nMedia general: {media_general:.1f} años")
print(f"Personas sobre la media: {sobre_media}")