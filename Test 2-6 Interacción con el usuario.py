#Ejemplo de imput()
print("Dime lo que sea...")
anything = input()
print("Hmm...", anything, "... ¿en serio?")
print()

#Cambio de tipo de datos
anything = float(input("Ingresa un número: "))
something = anything ** 2.0
print(anything, "a la potencia de 2 es", something)
print()

#Ejemplo de calculo de la hipotenusa
cateto_a = float(input("Ingresa la longitud del primer cateto: "))
cateto_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es:", (cateto_a**2 + cateto_b**2) ** .5)
print()

#Ejemplo de concatenación de cadenas
nombre = input("¿Me puedes dar tu nombre por favor? ")
apellido = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + nombre + " " + apellido + ".")
print()

#Ejemplo de replicación hacer un cuadrado
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
print()


var_a = float(input("ingresa un valor flotante para la variable \"a\" aquí: "))
var_b = float(input("ingresa un valor flotante para la variable \"b\" aquí: "))

print("El resultado de la suma es: " + str(var_a+var_b))
print("El resultado de la resta es: " + str(var_a-var_b))
print("El resultado de la multiplicación es: " + str(var_a*var_b))
print("El resultado de la división es: " + str(var_a/var_b))

print("\n¡Eso es todo, amigos!")

#LAB_1
X = float(input("ingresa un valor flotante para la variable \"X\" aquí: "))
Y = 1./(X+1./(X+1./(X+1./X)))
print("El resultado de Y:", Y)

#LAB_2
horas = int(input("Introduce las horas: "))
minutos = int(input("Introduce los minutos: "))
duracion = int(input("Introduce la duración en minutos: "))
horas = int(horas+(duracion//60))
if ((duracion+minutos)>60):
    horas = horas+1
if (horas>23):
    horas = horas%24
minutos = int((minutos+(duracion%60))-60)

print(horas,":", minutos)
