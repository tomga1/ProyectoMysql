import pymysql
import os
import requests
from tabulate import tabulate



def verificar(texto):
    while texto == "":
        print("Error, campo vacio")
        texto = input("Ingrese texto nuevamente: ")
    return texto

def input_numerico(frase):
    valor = input(frase)
    while True:
        try:
            valor = int(valor)
            break
        except ValueError:
            print("ERORR SOLO ENTEROS")
        valor = input("Ingrese nuevamente : " + frase)
    return valor    


def insertar(i,nom,prec):
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='',
                           db='local')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos VALUES (%s,%s,%s)", (i,nom,prec))
    conn.commit()
    conn.close()
    print("Productos salvado con exito ! ")


def mostrar():
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='',
                           db='local')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    nueva = []
    valor = calcular_precio
    for n in datos:
        p = [n[0],n[1],n[2],n[2]*valor]
    return datos

def calcular_precio():
    r= requests.get("https://dolarapi.com/v1/dolares")
    d = r.json()
    precio = d[0]["ventas"]
    return precio 



while True:
    print("""
      1) Insetar productos : 
      2) Ver productos : 
      3) Salir.
      """)
    opcion = input(">>>")
    if opcion == "1": 
        nombre = input("Ingrese nombre de producto : ")
        nombre = verificar(nombre)
        idi = input_numerico("Ingrese ID del producto: ")
        precio = input_numerico("Ingrese precio del producto: ")
        insertar(idi,nombre,precio)
    elif opcion == "2":
        r = mostrar()
        print(tabulate(r,["ID","NOMBRE","PRECIO","u$s","PRECIO $"],tablefmt="pretty"))
    elif opcion == "3" :
        print("Gracias por utlizar nuestro programa! ")
        break
    else: print("Error de opcion !")

    input("Toque ENTER para continuar...")
    os.system("cls")

