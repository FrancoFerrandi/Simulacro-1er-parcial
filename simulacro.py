# Franco Ferrandi 
# Comision 115 turno mañana


MENU = """ Seleccione el N° de la opcion deseada:
1) Cargar producto/s.
2) Buscar producto.
3) Ordenar inventario.
4) Mostrar producto más caro 
5) Mostrar producto más barato.
6) Mostrar productos con precio mayor a 15000.
7) Salir"""

# inventario = []
inventario = [
    ["producto_1", 12000, 10],
    ["producto_2", 25000, 5],
    ["producto_3", 15000, 20]
]


def mostrar_menu(menu: str) -> None:
    """
    Recibe un string con la varible menu y la imprime.
    Parametros: menu (str)
    Devuelve: None
    """
    print(menu)

def cargar_inventario(inventario: list) -> list:
    """
    Recibe parametro una lista("inventario"), genera una lista nueva con nombre de producto, precio y cantidad, y luego anida lista nueva en la lista recibida como parametro.
    Parametros: inventario (list)
    Salida: inventario (list)
    """

    lista_producto_nuevo = []

    producto_nombre = (input("Ingrese el nombre del producto: ").lower())
    while producto_nombre == "":
        producto_nombre = input("Nombre no valido. Ingrese el nombre del producto: ").lower()

    producto_precio = float(input("Ingrese el precio del producto: "))
    while producto_precio <= 0:
        producto_precio = float(input("Precio no valido. Ingrese el precio del producto: "))

    producto_cantidad = int(input("Ingrese la cantidad del producto que quiere agregar al stock: "))
    while producto_cantidad <= 0:
        producto_cantidad = int(input("Cantidad no valida. la cantidad del producto que quiere agregar al stock: "))

    lista_producto_nuevo = [producto_nombre, producto_precio, producto_cantidad]
    inventario.append(lista_producto_nuevo)

    return inventario

def mostrar_producto_seleccionado(inventario:list) -> None:
    """
    Recibe parametro una lista("inventario") busca dentro de ella nombre del producto buscado e imprime nombre, precio unitario y cantidad de stock del producto
    Parametros: inventario (list)
    Salida: None
    """
    producto_nombre = (input("Ingrese el nombre del producto: ").lower())
    while producto_nombre == "":
        producto_nombre = input("Nombre no valido. Ingrese el nombre del producto: ").lower()

    for n in range(len(inventario)):
        if inventario[n][0] == producto_nombre:

            producto = f"Producto: {inventario[n][0]}, precio unitario: {inventario[n][1]}, cantidad disponible: {inventario[n][2]}."
            print(producto)
            break

    else:
        producto = "El nombre del producto seleccionado no se encuentra en el inventario."
        print(producto)

def ordenar_inventario(inventario: list) -> None:
    """
    Recibe parametro inventario (list) y ordena los productos en función de su precio de manera ascendente usando el método de burbuja.
    Parametros: inventario (list)
    Return: None
    """
    n = len(inventario)
    for i in range(n):
        for j in range(0, n-i-1):
            if inventario[j][1] > inventario[j+1][1]:
                inventario[j], inventario[j+1] = inventario[j+1], inventario[j]

    print("Inventario ordenado por precio de manera ascendente:")
    for producto in inventario:
        print(f"Producto: '{producto[0]}', precio: {producto[1]}, cantidad: {producto[2]}")

def mostrar_producto_mas_caro(inventario: list) -> None:
    """
    Recibe parametro inventario (list) e imprime el nombre del producto mas caro y su precio unitario.
    Parametros: inventario (list)
    Return: None
    """
    producto_mas_caro = float('-inf')
    nombre_producto_mas_caro = ""

    for i in range(len(inventario)):
        if inventario[i][1] > producto_mas_caro:
            producto_mas_caro = inventario[i][1]
            nombre_producto_mas_caro = inventario[i][0]

    print(f"""Producto mas caro:
Nombre Producto: '{nombre_producto_mas_caro}', precio unitario: {producto_mas_caro}.""")
    

def mostrar_producto_mas_barato(inventario: list) -> None:
    """
    Recibe parametro inventario (list) e imprime el nombre del producto mas caro y su precio unitario.
    Parametros: inventario (list)
    Return: None
    """
    producto_mas_barato = float('inf')
    nombre_producto_mas_barato = ""

    for i in range(len(inventario)):
        if inventario[i][1] < producto_mas_barato:
            producto_mas_barato = inventario[i][1]
            nombre_producto_mas_barato = inventario[i][0]

    print(f"""Producto mas barato:
Nombre producto: '{nombre_producto_mas_barato}', precio unitario: {producto_mas_barato}""")

def mostrar_productos_precio_mayor(inventario:list) -> None:
    """
    Recibe parametro inventario (list) e imprime productos con un precio mayor a 15000.
    Parametros: inventario (list)
    Return: None
    """
    precio_mayor = 15000
    lista_precio_mayor = []

    for producto in inventario:
            if producto[1] > precio_mayor:
                lista_precio_mayor.append(producto)

    if lista_precio_mayor:
        print("Los productos con un precio mayor a $15000 son:")
        for prod in lista_precio_mayor:
            print(f"Producto: {prod[0]}, Precio: {prod[1]}, Cantidad: {prod[2]}")
    else:
        print("No hay productos con un precio mayor a $15000.")

def ejecutar_opcion(seguir:bool) -> bool:
    """
    Recibe parametro "seguir" (bool), se le pregunta un numero de opcion y ejecuta esa opcion(funcion) o finaliza el programa.
    Parametros: seguir (bool)
    Salida: seguir (bool)
    """
    opcion = int(input("Elige una opcion: "))
    while opcion < 1 or opcion > 7: 
        print("Opcion no valida")
        opcion = int(input("Elige una opcion(1-4): "))
        seguir = True
    if opcion == 1:
        print("Haz elegido la opcion 1")
        cargar_inventario(inventario)
        seguir = True
    elif opcion == 2:
        print("Haz elegido la opcion 2")
        mostrar_producto_seleccionado(inventario)
        seguir = True
    elif opcion == 3:
        print("Haz elegido la opcion 3")
        ordenar_inventario(inventario)
        seguir = True
    elif opcion == 4:
        print("Haz elegido la opcion 4")
        mostrar_producto_mas_caro(inventario)
        seguir = True
    elif opcion == 5:
        print("Haz elegido la opcion 5")
        mostrar_producto_mas_barato(inventario)
        seguir = True
    elif opcion == 6:
        print("Haz elegido la opcion 6")
        mostrar_productos_precio_mayor(inventario)
        seguir = True
    else:
        print("Haz elegido la opcion 7. Haz salido del sistema.")
        seguir = False
    return seguir

seguir = True
while seguir == True:
    mostrar_menu(MENU)
    seguir = ejecutar_opcion(seguir)