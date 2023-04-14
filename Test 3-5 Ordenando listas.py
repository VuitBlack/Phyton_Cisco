#Ordnear por el método BURBUJA
my_list = [8, 10, 6, 2, 4]  # lista a ordenar
swapped = True # Lo necesitamos verdadero (True) para ingresar al bucle while.
print("Lista original: ",my_list)
while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # ¡ocurrió el intercambio!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]


print("Lista ordenada: ",my_list)

#Ordnear por el método BURBUJA de modo interactivo te pregunta cuantos elementos quieres ordenar
my_list = []
swapped = True
num = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(num):
    val = float(input("Ingresa un elemento de la lista: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nOrdenada:")
print(my_list)

#Herramienta Python para ordenar la lista
my_list = [8, 10, 6, 2, 4]
print("Lista original: ",my_list)
my_list.sort()
print("Lista ordenada: ",my_list)
 