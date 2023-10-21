
"""

Usando pycharm , cree una Clase que permita registrar un producto. Contiene los siguientes atributos 
id, nombre, descripcion, costo, cantidad, precio_de_venta. Cree un metodo que permita registrar el 
producto y mediante un callback se le debe asignar el precio de venta de acuerdo a la siguiente formula: 
pv = costo/ (1- margen_de_venta), los productos al ser creados se guardaran en un diccionario. Cree un 
tercer metodo que permita imprimir el listado de productos. En la respuesta pegue el enlace del repositorio 
de Git Hub donde subió el ejercicio.

"""

import os

# Función para limpiar consola

def limpiar_consola():
    
    os.system('cls' if os.name == 'nt' else 'clear')

class Products:
    
    def __init__(self):
        self.productos = {}

    def RegisterProducts(self):
        
        limpiar_consola()
        
        # Validación de la id
       
        while True:
            id = input("Ingrese el ID del producto: ")
            if id:
                break
            else:
                print("\n" + "Error: debe ingresar un valor para el ID del producto. \n")

        # Validación del nombre

        while True:
            nombre = input("Ingrese el nombre del producto: ")
            if nombre:
                break
            else:
                print("\n" + "Error: debe ingresar un valor para el nombre del producto. \n")

        # Validación de la descripción
    
        while True:
            descripcion = input("Ingrese la descripción del producto: ")
            if descripcion:
                break
            else:
                print("\n" + "Error: debe ingresar un valor para la descripción del producto. \n")
        
        # Validación de costo
        
        while True:
            try:
                costo = float(input("Ingrese el costo del producto: "))
                break
            except ValueError:
                print("\n" + "Error: debe ingresar un valor numérico para el costo. \n")

        # Validación de cantidad
        
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad del producto: "))
                break
            except ValueError:
                print("\n" + "Error: debe ingresar un valor numérico entero para la cantidad. \n")

        margen_de_venta = 0.2  # Margen de venta predeterminado
        
        precio_venta = round(costo / (1 - margen_de_venta), 2)  # Se agrega un "2" para mostrar los decimales
        
        producto = {
            
            'id': id,
            'nombre': nombre,
            'descripcion': descripcion,
            'costo': costo,
            'cantidad': cantidad,
            'precio_venta': precio_venta
        }
        
        self.productos[id] = producto
        
        limpiar_consola()
        
        print("\n" + "Producto registrado exitosamente!")

    def PrintProducts(self):
        
        limpiar_consola()
        
        if not self.productos:
            
            print("\n" + "Aún no hay productos registrados.")
        else:
            
            print("\n" + "Listado de productos:")
            
            for id, producto in self.productos.items():
                
                print("\n" + f" Identificación: {id} \n Nombre: {producto['nombre']} \n Descripción: {producto['descripcion']} \n Costo: {producto['costo']} \n Cantidad: {producto['cantidad']} \n Margen de venta: {producto['precio_venta']} \n")

registro = Products()

# Menú

while True:
    
    print("\n" + " ------------- Menú --------------- ")
    print("|                                  |")
    print("|   1. Registrar productos         |")
    print("|   2. Ver productos registrados   |")
    print("|   3. Salir                       |")
    print("|                                  |")
    print(" ---------------------------------- ")
    
    opcion = input("\n" + "Ingrese una opción: ")
    
    if opcion == "1":
        
        registro.RegisterProducts()
        
    elif opcion == "2":
        
        registro.PrintProducts()
        
    elif opcion == "3":
        
        limpiar_consola()
        print("\n" + "Saliendo del programa... \n")
        break
    
    else:
        
        limpiar_consola()
        print("\n" + "Opción inválida. Por favor, intente nuevamente. \n")
        