# Almacena el actual número más grande aquí.
largest_number = -999999999
 
# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))
 
# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))
 
# Imprime el número más grande.
print("El número más grande es:", largest_number)

# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.
 
odd_numbers = 0
even_numbers = 0
 
# Lee el primer número.
number = int(input("Introduce un número o escribe 0 para detener: "))
 
# 0 termina la ejecución.
while number != 0:
    # Verificar si el número es impar.
    if number % 2 == 1:
        # Incrementar el contador de números impares odd_numbers.
        odd_numbers += 1
    else:
        # Incrementar el contador de números pares even_numbers.
        even_numbers += 1
    # Leer el siguiente número.
    number = int(input("Introduce un número o escribe 0 para detener: "))
 
# Imprimir resultados.
print("Conteo de números impares:", odd_numbers)
print("Conteo de números pares:", even_numbers)
 
#Empleando una variable counter para salir del bucle
counter = 5
while counter != 0:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)


#ADIVINA el número secreo o no podrás salir del Bucle

secret_number = 777

print(

+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
)
number = int(input("Introduce un número: "))
while number != secret_number:
    print("¡Ja Ja! ¡Estás atrapado en mi bucle!")
    number = int(input("Introduce un número nuevamente: "))
print(secret_number, "¡Bien hecho, muggle! Ahora eres libre") 

#Muestra las potencias de 2 del 1 al 16
power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2


import time
for i in range(5):
    print(i, "Mississippi")
    time.sleep(1)
print("¡Listos o no, ahí voy!")

#Realiza un programa que cambie la palabra ingresada a mayusculas y elminie todas las vocales, e imprima solo las consonantes

word = (input("Ingresa la palabra: "))
new_word=""
word = word.upper();

for letter in word:
    if letter == ('A'):
       continue
    elif letter == ('E'):
        continue
    elif letter ==('I'):
        continue
    elif letter ==('O'):
        continue
    elif letter ==('U'):
        continue
    else:    
        new_word = new_word + letter

print(new_word)



#Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores,
#  y generar la altura de la pirámide que se puede construir utilizando estos bloques.
#Nota: La altura se mide por el número de capas completas - si los constructores no tienen la cantidad 
# suficiente de bloques y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.
    
bloques = int(input("Ingresa el número de bloques: "))

altura = 0
incremento_Altura = 1

while incremento_Altura <= bloques:
    altura += 1
    bloques -= incremento_Altura
    incremento_Altura += 1

print("La altura de la pirámide es: ", altura)

#Hipótesis de Collatz

c0 = int(input("Ingresa c0: "))

if c0 > 1:
	steps = 0
	while c0 != 1:
		if c0 %2 != 0:
			cnew = 3 * c0 + 1
		else:
			cnew = c0 // 2
		print(c0)
		c0 = cnew
		steps += 1
	print("pasos =",steps)
else:
	print("Valor de c0 incorrecto")
	
#Crea un bucle for que cuente de 0 a 10, e imprima números impares en la pantalla. Usa el esqueleto de abajo:

for i in range(1, 11):
    if (i %2) != 0:
        print(i)

#Crea un bucle while que cuente de 0 a 10, e imprima números impares en la pantalla. Usa el esqueleto de abajo:

x = 1
while x < 11:
    if (x %2) != 0:
        print(x)
    x += 1

 #Crea un programa con un bucle for y una sentencia break. El programa debe iterar sobre los caracteres en una dirección de correo electrónico, 
 # salir del bucle cuando llegue al símbolo @ e imprimir la parte antes de @ en una línea.

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print (ch, end="")

#Crea un programa con un bucle for y una sentencia continue. 
# El programa debe iterar sobre una cadena de dígitos, reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla
for digit in "0165031806510":
    if digit == "0":
        print("x", end ="")
        continue
    print(digit, end="")


