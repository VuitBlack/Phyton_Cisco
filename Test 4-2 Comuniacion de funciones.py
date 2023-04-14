# Definir una funcion que reciba 3 argumentos e imprime esos parámtros
def my_function(a, b, c):
    print(a, b, c)
 
my_function(1, 2, 3)

#Ejemplo de funcion
def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)
 
introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")

#Paso de argumentos por palabra clave
def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)
 
introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

#Valores recurrentes como argumentos
def introduction(first_name, last_name="Smith"):
     print("Hola, mi nombre es", first_name, last_name)

introduction("Ricardo","Sandoval")