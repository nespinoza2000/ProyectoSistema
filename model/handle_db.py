import mysql.connector

#Aqui solo hago la conexion con la Base de Datos para las futuras consultas
class HandleDB():
    def __init__(self):
        # Reemplaza los valores con los de tu propia base de datos MySQL
        self._con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='user_management_db'
        )
        
        self._cur = self._con.cursor()
#Aqui finalizo con la inicializacion de la Base de Datos

#Aqui empiezan las consultas para tabla "users" de la Base de Datos
#Para obtener todos los usuarios
    def get_all(self):
        self._cur.execute("SELECT * FROM users")
        data = self._cur.fetchall()
        return data

#Para buscar un solo usuario
    def get_only(self, data_user):
        self._cur.execute("SELECT * FROM users WHERE username = %s", (data_user,))
        data = self._cur.fetchone()
        return data

#Para registrar un nuevo usuario en la tabla "users"
    def insert(self, data_user):
        query = "INSERT INTO users (id, firstname, lastname, username, password) VALUES (%s, %s, %s, %s, %s)"
        values = (data_user["id"], data_user["firstname"], data_user["lastname"], data_user["username"], data_user["password"])
        self._cur.execute(query, values)
        self._con.commit()
#Hasta aqui llegan las consultas para la tabla "users". Esto es netamente funcionalidad para el logueo

#Aqui empiezan las consultas para la tabla "materiales" en la base de datos
#Para traer los materiales de la tabla materiales de la base de datos
    def get_all_mat(self):
        self._cur.execute("SELECT * FROM materiales")
        data_mat = self._cur.fetchall()
        return data_mat

#Para traer los datos de un solo material
    def get_material_by_id(self, id_material):
        query = "SELECT * FROM materiales WHERE IdMat = %s"
        self._cur.execute(query, (id_material,))
        data_cliente = self._cur.fetchone()
        return data_cliente

#Para hacer un insert de datos en la tabla de materiales
    def insert_mat(self, data_mat):
        query = "INSERT INTO materiales (NombreMaterial, DescripcionMat, Precio, Cantidad) VALUES (%s, %s, %s, %s)"
        values = (data_mat["NombreMaterial"], data_mat["DescripcionMat"], data_mat["Precio"], data_mat["Cantidad"])
        try:
            self._cur.execute(query, values)
            self._con.commit()
            return True # Inserción exitosa
        except Exception as e:
            print(f"Error al registrar un nuevo material: {str(e)}")
            return False # Inserción fallida

#Para hacer un Update de datos dentro de la informacion de los materiales
    def update_material(self, id_material, new_data_mat):
        query = "UPDATE materiales SET NombreMaterial = %s, DescripcionMat = %s, Precio = %s, Cantidad = %s WHERE IdMat = %s"
        values = (new_data_mat["NombreMaterial"], new_data_mat["DescripcionMat"], new_data_mat["Precio"], new_data_mat["Cantidad"], id_material)
        self._cur.execute(query, values)
        self._con.commit()

#Para hacer un Delete de datos dentro de la informacion de un solo material
    def delete_material(self, id_material):
        query = "DELETE FROM materiales WHERE IdMat = %s"
        self._cur.execute(query, (id_material,))
        self._con.commit()
#Hasta aqui terminan las consultas para la tabla "materiales"

#Aqui inician las consultas a la tabla "clientes" en la base de datos
#Para traer los datos del cliente
    def get_cliente(self):
        self._cur.execute("SELECT * FROM clientes")
        data_cliente = self._cur.fetchall()
        return data_cliente

#Para traer los datos de un solo cliente
    def get_cliente_by_id(self, id_cliente):
        query = "SELECT * FROM clientes WHERE IdCliente = %s"
        self._cur.execute(query, (id_cliente,))
        data_cliente = self._cur.fetchone()
        return data_cliente

#Para hacer un insert de datos dentro de la tabla clientes
    def insert_cliente(self, data_cliente):
        query = "INSERT INTO clientes (NombreCliente, RUC, Direccion, Telefono) VALUES (%s, %s, %s, %s)"
        values = (data_cliente["NombreCliente"], data_cliente["RUC"], data_cliente["Direccion"], data_cliente["Telefono"])
        try:
            self._cur.execute(query, values)
            self._con.commit()
            return True  # Inserción exitosa
        except Exception as e:
            print(f"Error al registrar un nuevo cliente: {str(e)}")
            return False  # Inserción fallida

#Para hacer un Update de datos dentro de la informacion del cliente
    def update_cliente(self, id_cliente, new_data_cliente):
        query = "UPDATE clientes SET NombreCliente = %s, RUC = %s, Direccion = %s, Telefono = %s WHERE IdCliente = %s"
        values = (new_data_cliente["NombreCliente"], new_data_cliente["RUC"], new_data_cliente["Direccion"], new_data_cliente["Telefono"], id_cliente)
        self._cur.execute(query, values)
        self._con.commit()

#Para hacer un Delete de datos dentro de la informacion de un solo cliente
    def delete_cliente(self, id_cliente):
        query = "DELETE FROM clientes WHERE IdCliente = %s"
        self._cur.execute(query, (id_cliente,))
        self._con.commit()
#Hasta aqui terminan las consultas para la tabla "clientes"

#Aqui empiezan las consultas de la tabla "proveedores" de la base de datos
#Para traer los datos del proveedor
    def get_pro(self):
        self._cur.execute("SELECT * FROM proveedores")
        data_provee = self._cur.fetchall()
        return data_provee

#Para traer los datos de un solo proveedor
    def get_prove_by_id(self, id_pro):
        query = "SELECT * FROM proveedores WHERE IdPro = %s"
        self._cur.execute(query, (id_pro,))
        data_prove = self._cur.fetchone()
        return data_prove

#Para hacer un insert de datos dentro de la tabla proveedores
    def insert_proveedor(self, data_prove):
        query = "INSERT INTO proveedores (NombreProveedor, CIpro, RUC, Direccion, Telefono) VALUES (%s, %s, %s, %s, %s)"
        values = (data_prove["NombreProveedor"], data_prove["CIpro"], data_prove["RUC"], data_prove["Direccion"], data_prove["Telefono"])
        try:
            self._cur.execute(query, values)
            self._con.commit()
            return True # Inserción exitosa
        except Exception as e:
            print(f"Error al registrar un nuevo proveedor: {str(e)}")
            return False # Inserción fallida

#Para hacer un Update de datos dentro de la informacion del proveedor
    def update_proveedor(self, id_pro, new_data_provee):
        query = "UPDATE proveedores SET NombreProveedor = %s, CIpro = %s, RUC = %s, Direccion = %s, Telefono = %s WHERE IdPro = %s"
        values = (new_data_provee["NombreProveedor"], new_data_provee["CIpro"],  new_data_provee["RUC"], new_data_provee["Direccion"], new_data_provee["Telefono"], id_pro)
        self._cur.execute(query, values)
        self._con.commit()

#Para hacer un Delete de datos dentro de la informacion de un solo Proveedor
    def delete_proveedor(self, id_pro):
        query = "DELETE FROM proveedores WHERE IdPro = %s"
        self._cur.execute(query, (id_pro,))
        self._con.commit()
#Hasta aqui llegan las consultas a la tabla "camiones".

#Aqui empiezan las consultas a la tabla "camiones" en la base de datos.
#Para traer los datos del camion
    def get_cami(self):
        self._cur.execute("SELECT * FROM camiones")
        data_camion = self._cur.fetchall()
        return data_camion

#Para traer los datos de un solo camion
    def get_cami_by_id(self, id_cami):
        query = "SELECT * FROM camiones WHERE IdCamion = %s"
        self._cur.execute(query, (id_cami,))
        data_camion = self._cur.fetchone()
        return data_camion

#Para hacer un insert de datos dentro de la tabla camiones
    def insert_camion(self, data_camion):
        query = "INSERT INTO camiones (NroCamion, Marca, Modelo, Estado) VALUES (%s, %s, %s, %s)"
        values = (data_camion["NroCamion"], data_camion["Marca"], data_camion["Modelo"], data_camion["Estado"])
        try:
            self._cur.execute(query, values)
            self._con.commit()
            return True # Inserción exitosa
        except Exception as e:
            print(f"Error al registrar un nuevo camion: {str(e)}")
            return False # Inserción fallida

#Para hacer un Update de datos dentro de la informacion de un camion
    def update_camion(self, id_cami, new_data_cami):
        query = "UPDATE camiones SET NroCamion = %s, Marca = %s, Modelo = %s, Estado = %s WHERE IdCamion = %s"
        values = (new_data_cami["NroCamion"], new_data_cami["Marca"], new_data_cami["Modelo"], new_data_cami["Estado"], id_cami)
        self._cur.execute(query, values)
        self._con.commit()

#Para hacer un Delete de datos dentro de la informacion de un solo Camion
    def delete_camion(self, id_cami):
        query = "DELETE FROM camiones WHERE IdCamion = %s"
        self._cur.execute(query, (id_cami,))
        self._con.commit()
#Hasta aqui terminan las consultas para la tabla de "camiones".

#Aqui inician las consultas para la tabla "pedidos" de la base de datos
#Solo obtener el nombre de los proveedores para un <select> en la plantilla pedidos.html, compras.html y pagos.html
    def get_nombres_proveedores(self):
        self._cur.execute("SELECT NombreProveedor FROM proveedores")
        nombres_proveedores = self._cur.fetchall()
        return nombres_proveedores

#Para hacer un insert de datos dentro de la tabla pedidos
    def insert_pedido(self, data_pedido):
        forma_pago_map = {
            "option1": "Efectivo",
            "option2": "Transferencia bancaria",
            "option3": "Cheque con fecha diferida"
        }
        forma_pago = forma_pago_map.get(data_pedido["FormaPago"], "Forma de pago no especificada")
        query = "INSERT INTO pedidos (NombrePro, DescripPedido, FormaPago) VALUES (%s, %s, %s)"
        values = (data_pedido["NombrePro"], data_pedido["DescripPedido"], forma_pago)
        try:
            self._cur.execute(query, values)
            self._con.commit()
            return True  # Inserción exitosa
        except mysql.connector.Error as err:
            print(f"Error al registrar un nuevo pedido: {err}")
            return False  # Inserción fallida

#Para traer todos los pedidos imprimidos
    def get_pedidos(self):
        self._cur.execute("SELECT * FROM pedidos")
        data_pedido = self._cur.fetchall()
        return data_pedido

#Para traer los datos de un solo pedido
    def get_pedido_by_id(self, id_pedido):
        query = "SELECT * FROM pedidos WHERE IdPedido = %s"
        self._cur.execute(query, (id_pedido,))
        data_pedido = self._cur.fetchone()
        return data_pedido

#Para hacer un Update de datos dentro de la informacion de un pedido
    def update_pedido(self, id_pedido, new_data_pedido):
        query = "UPDATE pedidos SET DescripPedido = %s, FormaPago = %s WHERE IdPedido = %s"
        values = (new_data_pedido["DescripPedido"], new_data_pedido["FormaPago"], id_pedido)
        self._cur.execute(query, values)
        self._con.commit()

#Para hacer un Delete de datos dentro de la informacion de un solo pedido
    def delete_pedido(self, id_pedido):
        query = "DELETE FROM pedidos WHERE IdPedido = %s"
        self._cur.execute(query, (id_pedido,))
        self._con.commit()
#Hasta aqui llegan las consultas para la tabla de "pedidos"

#Desde aqui empiezan las consultas de la tabla "compras" de la base de datos
#Para obtener el nombre de los materiales para la plantilla compras.html
    def get_nombres_materiales_con_precio(self):
        self._cur.execute("SELECT NombreMaterial, Precio FROM materiales")
        nombres_materiales_con_precio = self._cur.fetchall()
        return nombres_materiales_con_precio

# Obtener el precio de un material específico
    def get_precio_material(self, nombre_material):
        query = "SELECT Precio FROM materiales WHERE NombreMaterial = %s"
        self._cur.execute(query, (nombre_material,))
        precio_material = self._cur.fetchone()
        return precio_material[3] if precio_material else None

#Para hacer un insert de datos dentro de la tabla compras
    def insert_compra(self, data_compra):
        query = "INSERT INTO compras (Proveedor, DetalleCompra, DescripCompra) VALUES (%s, %s, %s)"
        values = (data_compra["Proveedor"], data_compra["DetalleCompra"], data_compra["DescripCompra"])
        try:
            self._cur.execute(query, values)
            self._con.commit()
            return True  # Inserción exitosa
        except mysql.connector.Error as err:
            print(f"Error al imprimir ticket de compra {err}")
            return False  # Inserción fallida

#Para traer todos los tickets de compra imprimidos
    def get_compras(self):
        self._cur.execute("SELECT * FROM compras")
        data_compra = self._cur.fetchall()
        return data_compra

#Para hacer un delete de datos dentro de la informacion de una sola compra
    def delete_compra(self, id_compra):
        query = "DELETE FROM compras WHERE IdCompra = %s"
        self._cur.execute(query, (id_compra,))
        self._con.commit()

# Para traer todos los pagos realizados
    def get_pagos(self):
        self._cur.execute("SELECT * FROM pagos")
        data_pago = self._cur.fetchall()
        return data_pago

# Para obtener los datos de un solo pago
    def get_pago_by_id(self, id_pago):
        query = "SELECT * FROM pagos WHERE IdPago = %s"
        self._cur.execute(query, (id_pago,))
        data_pago = self._cur.fetchone()
        return data_pago

# Para hacer un insert de datos dentro de la tabla pagos
    def insert_pago(self, data_pago):
        forma_pago_map = {
            "option1": "Efectivo",
            "option2": "Transferencia bancaria",
            "option3": "Cheque con fecha diferida"
        }
        forma_pago = forma_pago_map.get(data_pago["FormaPago"], "Forma de pago no especificada")
        query = "INSERT INTO pagos (Proveedor, Monto, FormaPago) VALUES (%s, %s, %s)"
        values = (data_pago["Proveedor"], data_pago["Monto"], forma_pago)
        try:
            self._cur.execute(query, values)
            self._con.commit()
            return True  # Inserción exitosa
        except mysql.connector.Error as err:
            print(f"Error al registrar un nuevo pago: {err}")
            return False  # Inserción fallida
#Hasta aqui llegan las consultas para la tabla "compras"

#Estas son las consultas para la tabla "tareas" de la base de datos
#Para traer todas las tareas de la base de datos
    def get_tareas(self):
        self._cur.execute("SELECT * FROM tareas")
        data_tarea = self._cur.fetchall()
        return data_tarea

# Para obtener los datos de una sola tarea
    def get_tarea_by_id(self, id_tarea):
        query = "SELECT * FROM tareas WHERE IdTarea = %s"
        self._cur.execute(query, (id_tarea,))
        data_tarea = self._cur.fetchone()
        return data_tarea

#Para hacer un insert de datos dentro de la tabla tareas
    def insert_tarea(self, data_tarea):
        query = "INSERT INTO tareas (Tarea, Detalles) VALUES (%s, %s)"
        values = (data_tarea["Tarea"], data_tarea["Detalles"])
        try:
            self._cur.execute(query, values)
            self._con.commit()
            return True # Inserción exitosa
        except mysql.connector.Error as err:
            print(f"Error al agregar una tarea {err}")
            return False # Inserción fallida

#Para hacer un Update de datos dentro de la informacion de una tarea
    def update_tarea(self, id_tarea, new_data_tarea):
        query = "UPDATE tareas SET Tarea = %s, Detalles = %s WHERE IdTarea = %s"
        values = (new_data_tarea["Tarea"], new_data_tarea["Detalles"], id_tarea)
        self._cur.execute(query, values)
        self._con.commit()

#Para hacer un Delete de datos dentro de la informacion de una sola tarea
    def delete_tarea(self, id_tarea):
        query = "DELETE FROM tareas WHERE IdTarea = %s"
        self._cur.execute(query, (id_tarea,))
        self._con.commit()
#Hasta aqui llegan la consultas para la funcionalidad de tareas

#Aqui empiezan las consultas para la Base de Datos de la tabla "ventas".
#Para traer solo los nombres de los clientes
    def get_name_cliente(self):
        self._cur.execute("SELECT NombreCliente FROM clientes")
        nombres_clientes = self._cur.fetchall()
        return nombres_clientes

#Para traer solo los nombres de los materiales con su cantidad y precios
    def get_name_mat_pre_cant(self):
        self._cur.execute("SELECT NombreMaterial, Precio, Cantidad FROM materiales")
        nom_mat_pre_cant = self._cur.fetchall()
        return nom_mat_pre_cant

#Para visualizar los dados de la tabla ventas
    def get_ventas(self):
        self._cur.execute("SELECT * FROM ventas")
        data_venta = self._cur.fetchall()
        return data_venta

#Para visualizar un solo dato de la tabla ventas
    def get_venta_by_id(self, id_venta):
        query = "SELECT * FROM ventas WHERE IdVenta = %s"
        self._cur.execute(query, (id_venta,))
        data_venta = self._cur.fetchone()
        return data_venta

#Para hacer un insert de datos dentro de la tabla "ventas"
    def insert_ventas(self, data_venta):
        query = "INSERT INTO ventas (Cliente, Material, Detalle) VALUES (%s, %s, %s)"
        values = (data_venta["Cliente"], data_venta["Material"], data_venta["Detalle"])
        try:
            self._cur.execute(query, values)
            self._con.commit()
            return True # Inserción exitosa
        except mysql.connector.Error as err:
            print(f"Error al realizar una venta {err}")
            return False # Inserción fallida

#Para hacer un delete de datos dentro de la tabla "ventas"
    def delete_venta(self, id_ventas):
        query = "DELETE FROM ventas WHERE IdVenta = %s"
        self._cur.execute(query, (id_ventas,))
        self._con.commit()

    def __del__(self):
        self._con.close()