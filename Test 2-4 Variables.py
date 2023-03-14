#Ejemplo de creación de una variable
var = 1
account_balance = 1000.0
client_name = 'Jhon Dere'
print(var, account_balance, client_name)
var = var + 1
print(var)
print()

var = "3.8.5"
print("Python version: " + var)
print()

#Hallar la hipotenusa del triangulo a, b, c
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("Hallar la hipotenusa del triangulo a, b, c. Siendo a=3 y b=5")
print("c =", c)
print()

john = 3
mary = 5
adam = 6
total_apples = john+mary+adam
print("John =",john, 'Mary =',mary, "Adam =",adam)
print('Total apples =',total_apples)

# De millas a Km sabiendo 1milla=1.61Km
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")
print()

# Analiza y=3x3 - 2x2 + 3x - 1 para X=0, X=1 y X=-1

x = 0
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = -1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)


a = 6
b = 3
a /= 2 * b
print(a)