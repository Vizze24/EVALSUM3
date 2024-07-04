import csv
import random
import os
import time

os.system("cls")


pedidorandom=random.randrange(1,1000,1)


def cargar(pedido):
    while True:
        print("-"*35)
        print("BIENVENIDO AL PROGRAMA DE CATPREMIUN")
        print("-"*35)
        time.sleep(3)
        print("Antes de empezar es necesario cargar los archivos que se usaran\nRecuerda que si ya los tienes no debes cargar denuevo ya que perderas todo tu progreso\n")
        try:
            upload=int(input("Si tiene los achivos necesarios presione 1\nSi no los tienes y abre por primera vez este programa presione 2\nOpcion deseada: "))
        except ValueError:
            print("Ingrese digito correcto(numero del 1 al 2)")

        time.sleep(1)
        os.system("cls")

        print("Programa cargado correctamente...")
        time.sleep(1)
        os.system("cls")


        if upload==1:
            break
        elif upload==2:
            with open("pedidos.csv","w",newline="")as cargar:
                cargarcsv=csv.writer(cargar)
                cargarcsv.writerow(["Nro Pedido", "Cliente","Direccion","Sector","Saco 5KG","Saco 10KG","Saco 20KG"])
                cargarcsv.writerows([
                    [10,"Miguel Cortes","Los canelos 1042", "San Bernardo",1,1,0]

                ])
            break
        else:
            print("Ingrese un digito correcto")
    menu("pedidos.csv")


def registrarpedid(pedido):
    print("Ingrese los datos del pedido para agregarlo correctamente")
    time.sleep(2)
    with open("pedidos.csv","a",newline="")as registrar:
        pedidorandom=random.randint(1,1000)
        nom=input("Nombre: ")
        direc=input("Direccion: ")
        comuna=input("Sector:")
        while True:
            try: 
                saco5kg=int(input("Sacos 5kg: "))
                saco10kg=int(input("Sacos 10kg: "))
                saco20kg=int(input("Sacos 20kg: "))
                break
            except ValueError:
                print("Ingrese solo numeros, no caracteres ni caracteres especiales.")

        registerpedido=csv.writer(registrar)
        registerpedido.writerow([pedidorandom,nom,direc,comuna,saco5kg,saco10kg,saco20kg])
        
    print("Pedido agregado exitosamente")
    time.sleep(3)
    os.system("cls")

   

def listatodos(pedido):
    os.system("cls")
    with open("pedidos.csv","r",newline="") as todosp:
        mostrartodos=csv.DictReader(todosp)
        for fila in mostrartodos:
            nropedido=fila["Nro Pedido"]
            nom=fila["Cliente"]
            direc=fila["Direccion"]
            comun=fila["Sector"]
            saco5=int(fila["Saco 5KG"])
            saco10=int(fila["Saco 10KG"])
            saco20=int(fila["Saco 20KG"])
            print(f"Nro Pedido: {nropedido} /  Cliente: {nom} /  Direccion: {direc} /  Comuna: {comun} /  Saco 5kg: {saco5} /  Saco 10kg: {saco10} /  Saco 20kg: {saco20}")
            time.sleep(1)


def hojaderuta(pedido):
    
    buscador=input("Ingrese la comuna que desea ver en la hoja de ruta : ").lower()
    time.sleep(1)
    os.system("cls")
    print("HOJA DE RUTA")
    with open("pedidos.csv","r",newline="") as buscarcsv:
        buscadorbueno=csv.DictReader(buscarcsv)
        encontrados=False
        for fila in buscadorbueno:
            if fila["Sector"].lower()==buscador.lower():
                nropedi=int(fila["Nro Pedido"])
                nom=fila["Cliente"]
                direc=fila["Direccion"]
                sect=fila["Sector"]
                saco5=int(fila["Saco 5KG"])
                saco10=int(fila["Saco 10KG"])
                saco20=int(fila["Saco 20KG"])

                time.sleep(1)
                print("")
                print(f"Nro Pedido: {nropedi}  /  Cliente:{nom} / Comuna:{sect}  /  Saco 5Kg: {saco5} / Saco 10Kg: {saco10} /  Saco 20Kg: {saco20} ")
                encontrados=True
        if not encontrados:
            print("Comuna ingresada no encontrada")

     

def menu(pedido):
    while True:
        print("-"*35)
        print("MENU DE OPCIONES")
        print("-"*35)


        print("1. Registrar Pedido")
        print("2. Lista de todos los pedidos")
        print("3. Imprimir hoja de ruta")
        print("4. Salir del programa")
        try:
            opc=int(input("Ingrese la opcion deseada: "))
        except ValueError:
            print("Ingrese un digito correcto ")
        
        if opc==1:
            registrarpedid("pedidos.csv")
        elif opc==2:
            listatodos("pedidos.csv")
        elif opc==3:
            hojaderuta("pedidos.csv")
        elif opc==4:
            print("Saliendo del progama..")
            print("-"*35)
            print("MUCHAS GRACIAS POR USAR EL PROGAMA CATPREMIUN")
            print("-"*35)
            break
        else:
            print("Ingrese una opcion valida (recuerda que es del 1 al 4) ")
            continue



cargar("pedidos.csv")

