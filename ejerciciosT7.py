# Encuentra el error, crea una excepción y explica en un ménsaje:
print("Ejercicio 1:")
def ej1(n1,n2):
    try:
        r=n1/n2
    except ZeroDivisionError:
        print("Estás dividiendo un num entre 0!")

ej1(10,0)

print("==============================")
print("Ejercicio 2:")

lista = [1, 2, 3, 4, 5]
try:
    lista[10]
except IndexError:
    print("Error: El índice al que intentas acceder se encuentra fuera del rango, debes utilizar un número mayor o igual que cero y menor que la longitud de la lista.")

print("==============================")
print("Ejercicio 3:")

colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
try:
    colores['blanco']
except KeyError:
    print("Error: La clave del diccionario no se encuentra, debes probar con otra que sí exista.")

print("==============================")
print("Ejercicio 4:")

try:
    resultado = "20" + 15
except TypeError:
    print("Error: Sólo es posible sumar datos del mismo tipo, debes transformar el número a cadena o la cadena a número.")

print("==============================")
print("Ejercicio 4:")

elementos = [1, 5, -2]

def agregar_una_vez(lista, el):
    try:
        if el in lista:
            raise ValueError
        else:
            lista.append(el)
    except ValueError:
        print("Error: Imposible añadir elementos duplicados =>", el)
        

agregar_una_vez(elementos, 10)
agregar_una_vez(elementos, -2)
agregar_una_vez(elementos, "Hola")
print(elementos)