lista_op = []
titulo = ""
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


titulo = "~~~~~~~~~ MENU PRINCIPAL ~~~~~~~~~"
lista_op.append("1.- Stock marca")
lista_op.append("2.- Búsqueda por precio")
lista_op.append("3.- Listado de productos")
lista_op.append("4.- Salir")


productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
            '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'],
            'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2080Ti'],
            'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i5', 'integrada'],
            'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'Nvidia GTX1050'],
            '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'integrada'],
            '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
            'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
 }

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
 'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
 'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
 } 


def Stock_marca(marca):
    marca = marca.strip().lower()
    total_stock = 0
    for modelo in productos:
        marca_producto = productos[modelo][0].strip().lower()
        if marca_producto == marca:
            total_stock += stock.get(modelo, [0, 0])[1]
    print(f"El stock es: {total_stock}")

def Busqueda_de_precio(p_min, p_max):
    lista_resultados = []
    for modelo in productos:
        precio = stock[modelo][0]
        cantidad = stock[modelo][1]
        if p_min <= precio <= p_max and cantidad > 0:
            marca = modelo[modelo][0]
            lista_resultados.append(f"{marca}---{modelo}")
            if lista_resultados:
                lista_resultados.sort()
                print ("Los productos entre los precios ingresados son: ", lista_resultados)
            else:
                print("No hay notebooks en ese rango de precios.")

def salir():
    print("Saliendo del sistema.....")


op = 0
while op != 4:
    mostrar_menu(titulo, lista_op)
    op = validar_opcion(len(lista_op))
    if op == 1:
        marca_usuairo= input("Ingre se que marca quiere ver el stock:  ")
        Stock_marca(marca_usuairo)
    elif op == 2:
        p_min = int(input("Ingrese el valor der precio minimo:  "))
        p_max = int(input("Ingrese el valor del precio maximo:  "))
        Busqueda_de_precio(p_min, p_max)
    elif op == 4:
        salir()
        