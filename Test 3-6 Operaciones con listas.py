#Ejemplo de crar una lista a partir de otra
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3] #recordar que solo imprmira desde el inicio hasta el fin-1 por tanto solo el 8 y el 6
print(new_list)

#Programa que busca el elemento mayor en nuestra lista
my_list = [10, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

#Mismo programa resumido en código
my_list = [10, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
 
for i in my_list:
    if i > largest:
        largest = i
 
print(largest)

#Encontrar la posición de un elemento dentro de una lista
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False
 
for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break
 
if found:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")

#Comparar los números de dos listas y decir cuantos hay coincidentes
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0
 
for number in bets:
    if number in drawn:
        hits += 1
 
print(hits)

#Tu tarea es escribir un programa que elimine todas las repeticiones de números de la lista. 
# El objetivo es tener una lista en la que todos los números aparezcan no más de una vez.
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []
for number in my_list:  # Recorre todos los números de la lista original.
	if number not in new_list:  # Si el número no aparece dentro de la nueva lista...
		new_list.append(number)  # ...agregarlo aquí.
my_list = new_list[:]  # Crea una copia de new_list.
print("La lista con elementos únicos:")
print(my_list)
