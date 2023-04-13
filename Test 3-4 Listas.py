
numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo contenido de la lista original.
 
numbers[0] = 111
print("\nPrevio contenido de la lista:", numbers)  # Imprimiendo contenido de la lista anterior.
 
numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Nuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.
print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

print("\n Borrar el segundo elemento de la lista.")
del numbers[1]
print("Nueva longitud de la lista: ", len(numbers))
print(numbers)

hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.
print(hat_list)
hat_list[2] = int(input("Ingresa un número entero: "))

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
print("Elimina el último elemento de la lista.")
del hat_list[-1]

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("La nueva longitud de la lista es: ", len(hat_list))


print(hat_list)
hat_list.append(4)

print(len(hat_list))
print(hat_list)

###

hat_list.insert(0, 222)
print(len(hat_list))
print(hat_list)

#
# paso 1: crea una lista vacía llamada beatles;
Beatles = []
print("Paso 1:", Beatles)

# paso 2: emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison;

Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Paso 2:", Beatles)

# paso 3: emplea el buclefor y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best;
for members in range(2):
    Beatles.append(input("Nuevo miembro de la banda: "))
print("Paso 3:", Beatles)

# paso 4: usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista;
del Beatles[-1]
del Beatles[-1]
print("Paso 4:", Beatles)

# paso 5: usa el método insert() para agregar a Ringo Starr al principio de la lista.
Beatles.insert(0, "RingoStarr")
print("Paso 5:", Beatles)
print("Los Fav:",len(Beatles))

#Listas anidadas
my_list = [1, 'a', ["lista", 64, [0, 1], False]]
print (my_list)

#iterar una lista
my_list = ["blanco", "purpura", "azul", "amarillo", "verde"]
for color in my_list:
    print(color)