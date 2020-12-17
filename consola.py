#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Luis Miguel Gómez Londoño - 201729597
Universidad de los Andes 2020-20
Introduccion a Modelos Matematicos en Gestion Financiera
Profesor: Rene Meziat

ARCHIVO PRINCIPAL PARA CORRER EL PARCIAL.
Codigo fuente en: ./logic/parcial.py
Datos generados en: ./logic/data/
"""

import sys
sys.path.insert(1, './logic')
import parcial as logic

#Punto 1: En esta funcion se genera y se grafica un arbol binomial basado en los
#parametros ingresados por el usuario
#n: Numero de periodos
#t: Expiracion
#S: Precio inicial
#v: volatilidad
def punto1():
    print("Ejecutando Punto 1...")
    n = int(input("Ingrese el numero de periodos n: "))
    S = int(input("Ingrese el precio inicial S0: "))
    u = float(input("Ingrese valorizacion u: "))
    d = float(input("Ingrese depreciacion d: "))
    p = float(input("Ingrese la probabilidad: "))
    logic.ArbolBinomial(n, S, u, d, p, True)
    print("Punto 1 ejecutado.")
    
def punto2():
    print("Ejecutando Punto 2...")
    n = int(input("Ingrese el numero de periodos n: "))
    S = int(input("Ingrese el precio inicial S0: "))
    u = float(input("Ingrese valorizacion u: "))
    d = float(input("Ingrese depreciacion d: "))
    r = float(input("Ingrese la tasa libre de riesgo r: "))
    logic.ArbolTLR(n, S, u, d, r, True)
    print("Punto 2 ejecutado.")
    
def punto3():
    print("Ejecutando Punto 3...")
    n = int(input("Ingrese el numero de periodos n: "))
    sigma = float(input("Ingrese el valor de sigma: "))
    logic.evolucionPreciosSimetrico(n, sigma, True)
    print("Punto 3 ejecutado.")

def punto4():
    print("Ejecutando Punto 4...")
    n = int(input("Ingrese el numero de periodos n: "))
    sigma = float(input("Ingrese el valor de sigma: "))
    ascenso = float(input("Ingrese la probabilidad de ascenso: "))
    descenso = float(input("Ingrese la probabilidad de descenso: "))
    p = float(input("Ingrese la probabilidad: "))
    logic.evolucionPrecioGeneral(n, sigma, ascenso, descenso, p, True)
    print("Punto 4 ejecutado.")

def punto5():
    print("Ejecutando Punto 5...")
    n = int(input("Ingrese el numero de periodos n: "))
    ascenso = int(input("Ingrese el ascenso: "))
    p = float(input("Ingrese la probabilidad: "))
    t = int(input("Cuantos tiempos de parada hay: "))
    TPS = []
    for i in range(t):
        tp = int(input("Ingrese el tiempo de parada {}: ".format(i+1)))
        decision = int(input("Ingrese la decision (+1 o -1): "))
        TPS.append(tp)
        TPS.append(decision)
    nivel = int(input("Ingrese el nivel: "))
    logic.tiempoAlcance(n, ascenso, p, nivel, TPS, True)
    print("Punto 5 ejecutado.")

def punto6():
    print("Ejecutando Punto 6...")
    logic.sacar10Simulaciones()
    print("Punto 6 ejecutado.")

def punto7():
    print("Ejecutando Punto 7...")
    n = int(input("Ingrese el numero de periodos n: "))
    sigma = float(input("Ingrese el valor de sigma: "))
    r = float(input("Ingrese el valor de r: "))
    deltaN = []
    for i in range(n-1):
        dActual = float(input("   Ingrese el valor del deltaN en {}: ".format(i+1)))
        deltaN.append(dActual)
    logic.gestion_de_portafolio(n, sigma, r, deltaN)
    print("Punto 7 ejecutado.")

def punto8():
    print("Ejecutando Punto 8...")
    n = int(input("Ingrese el n: "))
    u = float(input("Ingrese el u: "))
    d = float(input("Ingrese la d: "))
    r = float(input("Ingrese el r: "))
    VN = []
    for i in range(n+1):
        v = float(input("Ingrese el valor {}:".format(i+1)))
        VN.append(v)
    logic.valoracionDerivado(u, d, r, VN)
    print("Punto 8 ejecutado.")

def punto9():
    print("Ejecutando Punto 9...")
    
    print("Punto 9 ejecutado.")

def punto10():
    print("Ejecutando Punto 10...")
    
    print("Punto 10 ejecutado.")

    
def imprimir_menu_principal():
    """ Imprime los items del menú principal de la aplicación
    """
    print("\n          Puntos Parcial Final:\n")
    print("\n Ingrese el numero del punto que desee ejecutar. \n")
    print("(1) Punto 1: Modelo Arbol Binomial.")
    print("(2) Punto 2: Simulacion con riesgo neutral.")
    print("(3) Punto 3: Camino aleatorio simetrico de precios por formula.")
    print("(4) Punto 4: Camino aleatorio no simetrico de precios por formula.")
    print("(5) Punto 5: Tiempos de alcance.")
    print("(6) Punto 6: 10 simulaciones.")
    print("(7) Punto 7: Gestion del portafolio tipo delta.")
    print("(8) Punto 8: Valoracion del derivado.")
    print("(9) Punto 9: Operacion delta que replica el derivado.")
    print("(10) Punto 10: Demostracion martingala.")
    print("(11) Salir")
    
def iniciar_aplicacion():
    salir = False
    while(not salir):
        imprimir_menu_principal()
        opcion = int(input("Ingrese la opción deseada: "))
    
        if opcion == 1:
            punto1()
        elif opcion == 2:
            punto2()
        elif opcion == 3:
            punto3()
        elif opcion == 4:
            punto4()
        elif opcion == 5:
            punto5()
        elif opcion == 6:
            punto6()
        elif opcion == 7:
            punto7()
        elif opcion == 8:
            punto8()
        elif opcion == 9:
            punto9()
        elif opcion == 10:
            punto10()
        elif opcion == 11:
            salir = True
            print("EJECUCION TERMINADA.")
        else:
            print("El valor ingresado no es válido.")

iniciar_aplicacion()
    