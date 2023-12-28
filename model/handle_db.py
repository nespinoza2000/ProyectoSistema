import mysql.connector

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

    def get_all(self):
        self._cur.execute("SELECT * FROM users")
        data = self._cur.fetchall()
        return data

    def get_only(self, data_user):
        self._cur.execute("SELECT * FROM users WHERE username = %s", (data_user,))
        data = self._cur.fetchone()
        return data

    def insert(self, data_user):
        query = "INSERT INTO users (id, firstname, lastname, username, password) VALUES (%s, %s, %s, %s, %s)"
        values = (data_user["id"], data_user["firstname"], data_user["lastname"], data_user["username"], data_user["password"])
        self._cur.execute(query, values)
        self._con.commit()

#Para traer los materiales de la tabla materiales de la base de datos
    def get_all_mat(self):
        self._cur.execute("SELECT * FROM materiales")
        data_mat = self._cur.fetchall()
        return data_mat

#Para hacer un insert de datos en la tabla de materiales
    def insert_mat(self, data_mat):
        query = "INSERT INTO materiales (NombreMaterial, DescripcionMat, Precio, Cantidad) VALUES (%s, %s, %s, %s)"
        values = (data_mat["NombreMaterial"], data_mat["DescripcionMat"], data_mat["Precio"], data_mat["Cantidad"])
        self._cur.execute(query, values)
        self._con.commit()

#Para traer los datos del cliente
    def get_cliente(self):
        self._cur.execute("SELECT * FROM clientes")
        data_cliente = self._cur.fetchall()
        return data_cliente

#Para traer los datos de un solo cliente
    def get_cliente_by_id(self, id_cliente):
        query = "SELECT * FROM clientes WHERE ID = %s"
        self._cur.execute(query, (id_cliente,))
        data_cliente = self._cur.fetchone()
        return data_cliente


#Para hacer un insert de datos dentro de la tabla clientes
    def insert_cliente(self, data_cliente):
        query = "INSERT INTO clientes (NombreCliente, RUC, Direccion, Telefono) VALUES (%s, %s, %s, %s)"
        values = (data_cliente["NombreCliente"], data_cliente["RUC"], data_cliente["Direccion"], data_cliente["Telefono"])
        self._cur.execute(query, values)
        self._con.commit()

#Para hacer un Update de datos dentro de la informacion del cliente
    def update_cliente(self, new_data_cliente):
        query = "UPDATE clientes SET NombreCliente = %s, RUC = %s, Direccion = %s, Telefono = %s WHERE ID = %s"
        values = (new_data_cliente["NombreCliente"], new_data_cliente["RUC"], new_data_cliente["Direccion"], new_data_cliente["Telefono"])
        self._cur.execute(query, values)
        self._con.commit()

    def __del__(self):
        self._con.close()