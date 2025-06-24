lista_op = []
titulo = ""
stock_maximo = 20 
diccionario_nombres = {}


def mostrar_menu(titulo, lista_op):
    print(titulo)
    for opcion in lista_op:
        print(opcion)


def validar_opcion(cantidad_op):
    ingreso = True
    while ingreso:
        try:
            op = int(input("Ingrese la opcion selecionada:  "))
            if op <= 0 or op > cantidad_op:
                print("Error:  opcion invalida ")
            else:
                ingreso = False
                return op
        except ValueError:
            print("ERROR: Ingrese un número")


reserva_zapatillas = []
cantidad_reservas = {}
lista_claves = ["EstoyEnListaDeReserva"]
def validacion_usuairo_commpra():
    continuar = True
    seguir = True
    while seguir:
        nombre_comprador = input("Ingrese el nombre del comprador: ")
        if nombre_comprador in diccionario_nombres:
            print("El usuario ya esta registrado: \n"
                f"{diccionario_nombres} \n")
            return
        else:
            while continuar:
                op_clave = input("Desea colocar una clave al usuario (si/no):  ")
                if op_clave == "si":
                    clave_ = input("Ingrese la clave:  ")
                    if clave_ in lista_claves:
                        print("La clave es correcta")
                        continuar = False
                        diccionario_nombres[nombre_comprador] = lista_claves
                        
                    else:
                        print("La clave es incorrecta")
                        continuar = False 
                        return
                elif op_clave == "no":
                    print("no ingresara con un usuario, se ingresara como invitado ")
                    seguir = False
                    continuar = False
                    diccionario_nombres[nombre_comprador] = lista_claves
                else:
                    print("Ingrese un caracter de si o no")
        compra_zapatillas = input("¿Desea reservar una zapatilla? (si/no):  ")        
        if compra_zapatillas == "si":
            print("ya reservo una zapatilla.")
            reserva_zapatillas.append(nombre_comprador)
            cantidad_reservas[nombre_comprador] = 1
            print(cantidad_reservas)
            seguir = False
        elif compra_zapatillas== "no":
            print("No se reservo ninguna zapatilla:")
    return nombre_comprador


def buscar_reservas(nombre_comprador):
    print(cantidad_reservas)
    if nombre_comprador in reserva_zapatillas:
        reserva_vip = input("Desea pagar un extra por una reservaVIP (si/no):  ")
        if reserva_vip == "si":
            print(" Se agregaron dos reservas ")
            cantidad_reservas[nombre_comprador] = 2
            print(cantidad_reservas)
        elif reserva_vip == "no":
            print(" Solo se hizo una reserva ")
            print(cantidad_reservas)
    else:
        print("No hay ninguna reserva  ")


def mostrar_stock(cantidad_reservas):
        for nombre_comprador in cantidad_reservas:
            print(f"El stock reservado por {nombre_comprador} es: {cantidad_reservas[nombre_comprador]}")
        suma_reservas= sum(cantidad_reservas.values())
        stock_disponible=stock_maximo - suma_reservas
        print (f"El stock disponible es: {stock_disponible}")
        return stock_disponible


def salir():
    print("    Saliendo de la reserva    ")


titulo = "~~~~~~~~~ TOTEM DE AUTENTICACION DE RESERVAS ~~~~~~~~~"
lista_op.append("1.- Reservar zapatillas")
lista_op.append("2.- Buscar reserva de zapatillas")
lista_op.append("3.- Ver stock de reservas")
lista_op.append("4.- Salir ")

op = 0
while op != 4:
    mostrar_menu(titulo, lista_op)
    op = validar_opcion(len(lista_op))
    if op == 1:
        nombre = validacion_usuairo_commpra()
    elif op == 2:
        buscar_reservas(nombre)
    elif op == 3:
        mostrar_stock(cantidad_reservas)
    elif op == 4:
        salir()
        
