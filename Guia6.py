# Ejercicio 1

import math

def imprimir_hola_mundo ():
    print ("Hola Mundo!")

def imprimir_un_verso():
    print ("Llega el domingo voy a ver al campeón \n River vos sos mi locura \n Llevo los trapos para alentarte a vos \n Me chupa un h*evo la yuta \n Yo soy de River porque tenemos aguante \n No como boca son todos vigilantes \n Esta tribuna los noventa minutos \n No para de alentarte…")

def raizDe2():
   c = round(2**0.5, ndigits=4)
   print(c)

def factorial_2() -> float :
    print(math.factorial(2))

def perimetro() -> float:
   print  (2 * math.pi)

#Ejercicio 2

def imprimir_saludo (nombre: str):
    print ("Hola " + nombre)

def raiz_cuadrada_de (numero: int): 
    print (numero**0.5)

def fahrenheit_a_celsius (t: float) -> float:
    res = ((t-32) * 5)/9
    print (res)

def imprimir_dos_veces(estribillo: str):
    print (estribillo * 2) 

def es_multiplo_de (n: float,m: float) -> bool: #Return ya que devuelve un bool
    resultado:bool = True
    if n % m == 0:
        resultado = True
    else:
        resultado = False
    
    return resultado
#resolucion 2 (mas corta):
# resultado:bool = n % m == 0

def es_par (numero: int) -> None: #None ya que no devuelve nada, solo muestra por pantalla
    res:bool = es_multiplo_de(numero,2)
    print (res)

def cantidad_de_pizzas (comensales: float,min_cant_de_porciones: float):
    res = (comensales * min_cant_de_porciones) // 8
    print (res)


#Ejercicio 3
def alguno_es_0 (numero1: float, numero2: float):
    res = (numero1 == 0 and numero2 != 0) or (numero2 == 0 and numero1 != 0)
    print (res)

def ambos_son_0 (numero1: float, numero2: float):
    res = (numero1 == 0 and numero2 == 0)
    print (res) 

def es_nombre_largo (nombre: str) -> bool:
    res = 3 <= len(nombre) <= 8
    print (res)

def es_bisiesto(año: int):
    res = año % 400 == 0 or año % 4 == 0 and año % 100 != 0
    print (res)


#Ejercicio 4

