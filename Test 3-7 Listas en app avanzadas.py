#Crea una lista que calcule los cuadrados de los 10 primeros números:
squares = [x ** 2 for x in range(10)]
print (squares)
#Crea una lista de 8 elementos que coincidan con las primeras 8 potencias de 2:
twos = [2 ** i for i in range(8)]
print(twos)
#Crea una lista con los elementos impares de squares
odds = [x for x in squares if x % 2 != 0 ]
print(odds)

#Ejemplo de matriz
table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]
 
print(table)
print(table[0][0])  # output: ':('
print(table[0][3])  # output: ':)'


