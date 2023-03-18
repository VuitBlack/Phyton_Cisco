var = 0  # Asignando 0 a var
print(var != 0)
 
var = 1  # Asignando 1 a var
print(var != 0)

n = int(input("Ingresa un número: "))
print(100<=n)

# Sentencia IF
sheep_counter = int(input("Input the number of sheeps: "))
if sheep_counter >= 120:        #se ejecutan las sentencias de abajos si es >= a 120
    print("make_a_bed")
    print("take_a_shower")
    print("sleep_and_dream")
print("feed_the_sheepdogs")     #Siempre se ejecuta no pertence al IF

# Sentencia IF-ELSE
the_weather_is_good = int(input("If weather is good input number 1: "))
if the_weather_is_good == 1:
    print("go_for_a_walk")
else:
    print("go_to_a_theater")
print("have_lunch")

#Comenzaremos con el caso más simple - ¿cómo identificar el mayor de los dos números?:

number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
if number1 > number2:           # Elige el número más grande
    larger_number = number1
else:
    larger_number = number2
print("El número más grande es:", larger_number) # Imprime el resultado

#Como saber el número más grande de 3 variables
number1= int(input("Ingresa el 1 número: "))
number2= int(input("Ingresa el 2 número: "))
number3= int(input("Ingresa el 3 número: "))

largest_number = max(number1,number2,number3)

print("El número mas grande es: ",largest_number)
