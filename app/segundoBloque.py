#1 - Escribe un programa que pida a la persona usuaria que proporcione dos números y muestre el número más grande.
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
print(f"El número mayor es: {max(num1, num2)}")
#2 - Escribe un programa que solicite el porcentaje de crecimiento de producción de una empresa e informe si hubo un crecimiento (porcentaje positivo) o una disminución (porcentaje negativo).
porcentaje = float(input("Porcentaje de crecimiento: "))
if porcentaje > 0:
    print("Hubo crecimiento (positivo)")
elif porcentaje < 0:
    print("Hubo disminución (negativo)")
else:
    print("No hubo cambio")
#3 - Escribe un programa que determine si una letra proporcionada por la persona usuaria es una vocal o una consonante.
letra = input("Ingresa una letra: ").lower()
if letra in ('a', 'e', 'i', 'o', 'u'):
    print("Es vocal")
else:
    print("Es consonante")
#4 - Escribe un programa que lea valores promedio de precios de un modelo de automóvil durante 3 años consecutivos y muestre el valor más alto y más bajo entre esos tres años.
precios = [float(input(f"Año {i+1}: ")) for i in range(3)]
print(f"Valor más alto: {max(precios)}")
print(f"Valor más bajo: {min(precios)}")
#5 - Escribe un programa que pregunte sobre el precio de tres productos e indique cuál es el producto más barato para comprar.
productos = [float(input(f"Precio producto {i+1}: ")) for i in range(3)]
print(f"El más barato cuesta: {min(productos)}")
#6 - Escribe un programa que lea tres números y los muestre en orden descendente.
numeros = [float(input(f"Número {i+1}: ")) for i in range(3)]
print(sorted(numeros, reverse=True))
#7 -Escribe un programa que pregunte en qué turno estudia la persona usuaria ("mañana", "tarde" o "noche") y muestre el mensaje "¡Buenos Días!", "¡Buenas Tardes!", "¡Buenas Noches!" o "Valor Inválido!", según el caso.
turno = input("Turno (mañana/tarde/noche): ").lower()
if turno == "mañana":
    print("¡Buenos Días!")
elif turno == "tarde":
    print("¡Buenas Tardes!")
elif turno == "noche":
    print("¡Buenas Noches!")
else:
    print("Valor Inválido!")
#8 - Escribe un programa que solicite un número entero a la persona usuaria y determine si es par o impar. Pista: Puedes usar el operador módulo (%).
numero = int(input("Número entero: "))
print("Par" if numero % 2 == 0 else "Impar")
#9 - Escribe un programa que pida un número a la persona usuaria y le informe si es entero o decimal.
numero = float(input("Número: "))
print("Entero" if numero == int(numero) else "Decimal")
#Momento de los proyectos
#10 - Un programa debe ser escrito para leer dos números y luego preguntar a la persona usuaria qué operación desea realizar. El resultado de la operación debe incluir información sobre el número, si es par o impar, positivo o negativo, e entero o decimal.
a = float(input("Primer número: "))
b = float(input("Segundo número: "))
operacion = input("Operación (+, -, *, /): ")

if operacion == '+':
    resultado = a + b
elif operacion == '-':
    resultado = a - b
elif operacion == '*':
    resultado = a * b
elif operacion == '/':
    resultado = a / b if b != 0 else "Indefinido"

paridad = "par" if resultado % 2 == 0 else "impar" if isinstance(resultado, int) else "decimal"
signo = "positivo" if resultado > 0 else "negativo" if resultado < 0 else "cero"
tipo = "entero" if isinstance(resultado, int) else "decimal"

print(f"Resultado: {resultado} | {paridad} | {signo} | {tipo}")
#11 - Escribe un programa que pida a la persona usuaria tres números que representan los lados de un triángulo. El programa debe informar si los valores pueden utilizarse para formar un triángulo y, en caso afirmativo, si es equilátero, isósceles o escaleno. Ten en cuenta algunas sugerencias:
#Tres lados forman un triángulo cuando la suma de cualesquiera dos lados es mayor que el tercero;
#Triángulo Equilátero: tres lados iguales;
#Triángulo Isósceles: dos lados iguales;
#Triángulo Escaleno: tres lados diferentes.
a, b, c = [float(input(f"Lado {i+1}: ")) for i in range(3)]

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilátero")
    elif a == b or a == c or b == c:
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("No forman triángulo")
#12 - Un establecimiento está vendiendo combustibles con descuentos variables. Para el etanol, si la cantidad comprada es de hasta 15 litros, el descuento será del 2% por litro. En caso contrario, será del 4% por litro. Para el diésel, si la cantidad comprada es de hasta 15 litros, el descuento será del 3% por litro. En caso contrario, será del 5% por litro. El precio por litro de diésel es de R$ 2,00 y el precio por litro de etanol es de R$ 1,70. Escribe un programa que lea la cantidad de litros vendidos y el tipo de combustible (E para etanol y D para diésel) y calcule el valor a pagar por el cliente. Ten en cuenta algunas sugerencias:
#El valor del descuento será el producto del precio por litro, la cantidad de litros y el valor del descuento.
#El valor a pagar por un cliente será el resultado de la multiplicación del precio por litro por la cantidad de litros menos el valor del descuento resultante del cálculo.
litros = float(input("Litros vendidos: "))
tipo = input("Tipo (E/D): ").upper()

if tipo == 'E':
    precio = 1.70
    descuento = 0.02 if litros <= 15 else 0.04
else:
    precio = 2.00
    descuento = 0.03 if litros <= 15 else 0.05

total = litros * precio * (1 - descuento)
print(f"Total a pagar: R$ {total:.2f}")
#13 - En una empresa de venta de bienes raíces, debes crear un código que analice los datos de ventas anuales para ayudar a la dirección en la toma de decisiones. El código debe recopilar los datos de cantidad de ventas durante los años 2022 y 2023 y calcular la variación porcentual. A partir del valor de la variación, se deben proporcionar las siguientes sugerencias:
#Para una variación superior al 20%: bonificación para el equipo de ventas.
#Para una variación entre el 2% y el 20%: pequeña bonificación para el equipo de ventas.
#Para una variación entre el 2% y el -10%: planificación de políticas de incentivo a las ventas.
#Para bonificaciones inferiores al -10%: recorte de gastos.
ventas_2022 = float(input("Ventas 2022: "))
ventas_2023 = float(input("Ventas 2023: "))
variacion = (ventas_2023 - ventas_2022) / ventas_2022 * 100

if variacion > 20:
    print("Bonificación para el equipo")
elif 2 <= variacion <= 20:
    print("Pequeña bonificación")
elif -10 <= variacion < 2:
    print("Planificación de incentivos")
else:
    print("Recorte de gastos")