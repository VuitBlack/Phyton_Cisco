#Cálculo de IMC o BMI
# La \ significa que si se termina una línea de código con el, Python entenderá que la línea continua en la siguiente.
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(92, 1.83))

#Igual pero en Sistema Inglés
def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
 
 
def lb_to_kg(lb):
    return lb * 0.4535923
 
 
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
 
    return weight / height ** 2
 
 
print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))

#Teorema de pitágoras
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
 
def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))

#El área de un triangulo
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
 
def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5
 
def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)
 
print("El área del triangulo es: ",area_of_triangle(1., 1., 2. ** .5))

#Factoriales
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
 
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
 
print("\nFactoriales entre 0 y 5")
for n in range(1, 6): # probando
    print(n, factorial_function(n))

#Números de Fibonacci
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
 
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum
 
print("\nNúmeros de Fibonacci entre 1 y 10") 
for n in range(1, 10): # probando
    print(n, "->", fib(n))