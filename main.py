from fastapi import FastAPI, HTTPException, Request, Response, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from controller.user import User
from lib.check_passw import check_user
from model.handle_db import HandleDB
import mysql.connector

app = FastAPI()

template = Jinja2Templates(directory="./view")

@app.get("/", response_class=HTMLResponse)
def root(req: Request):
    return template.TemplateResponse("index.html", {"request": req})

@app.post("/", response_class=HTMLResponse)
def root(req: Request):
    return template.TemplateResponse("index.html", {"request": req})

@app.get("/signup", response_class=HTMLResponse)
def signup(req: Request):
    return template.TemplateResponse("signup.html", {"request": req})

#No tocar este fragmento de codigo
@app.post("/user", response_class=HTMLResponse)
def user(req: Request, username: str = Form(), password: str = Form()):
        verify = check_user(username, password)
        if verify:
            return template.TemplateResponse(
                "employd.html", {"request": req, "data_user": verify}
            )
        raise HTTPException(status_code=401, detail="Unauthorized")

@app.get("/back-to-user")
def back_to_user():
    return RedirectResponse(url="/get-user", status_code=302)

@app.get("/get-user", response_class=HTMLResponse)
def get_user(req: Request):
    return template.TemplateResponse("employd.html", {"request": req, "data_user": True})

#No tocar esta linea de codigo
@app.post("/data_processing")
def data_processing(
    req: Request,
    firstname: str = Form(),
    lastname: str = Form(),
    username: str = Form(),
    # country: str = Form(),
    password: str = Form()
):
    data_user = {
        "firstname": firstname,
        "lastname": lastname,
        "username": username,
        # "country": country,
        "password": password
    }
    user = User(data_user)
    try:
        user.create_user()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear usuario: {str(e)}")
    return RedirectResponse(url="/", status_code=302)

#Desde aqui empieza todo lo referente a materiales 
@app.get("/registrarMat")
def registro_mat(req: Request):
    return template.TemplateResponse("materiales.html", {"request": req})

@app.post("/CargarM")
def cargar_mat(
    req: Request,
    nombrematerial: str = Form(...),
    desc: str = Form(...),
    precio: int = Form(...),
    cantidad: int = Form(...)
):
    data_mat = {
        "NombreMaterial": nombrematerial,
        "DescripcionMat": desc,
        "Precio": precio,
        "Cantidad": cantidad
    }
    handle_db = HandleDB()
    material_registrado = handle_db.insert_mat(data_mat)
    del handle_db
    print(material_registrado)
    response = template.TemplateResponse(
        "material_registrado.html", {"request": req, "data_user": True, "material_registrado": material_registrado}) #Comando para volver al menu del empleado
    response.set_cookie(key="session", value="some_session_token")
    return response

@app.get("/verMat")
def verMat(req: Request):
    handle_db = HandleDB()
    materiales = handle_db.get_all_mat()
    return template.TemplateResponse("ver_materiales.html", {"request": req, "materiales": materiales})

@app.get("/EditarMaterial/{IdMat}")
def show_edit_material(req: Request, IdMat: int):
    handle_db = HandleDB()
    material = handle_db.get_material_by_id(IdMat) # Cambiar a get_material_by_id para obtener un material específico
    del handle_db
    return template.TemplateResponse("editar_material.html", {"request": req, "material": material})

@app.post("/EditarMaterial/{IdMat}/update")
def update_material(
    req: Request,
    IdMat: int,
    nombrematerial: str = Form(...),
    desc: str = Form(...),
    precio: int = Form(...),
    cantidad: int = Form(...)
):
    new_data_mat = {
        "NombreMaterial": nombrematerial,
        "DescripcionMat": desc,
        "Precio": precio,
        "Cantidad": cantidad
    }
    handle_db = HandleDB()
    handle_db.update_material(IdMat, new_data_mat)
    del handle_db
    return RedirectResponse(url="/verMat", status_code=302)

@app.get("/BorrarMaterial/{IdMat}/delete")
def delete_material(IdMat: int):
    handle_db = HandleDB()
    handle_db.delete_material(IdMat)
    del handle_db
    return RedirectResponse(url="/verMat", status_code=302)
#Aqui acaba toda las funcionalidades para materiales

#Desde aqui empieza todo lo referente a clientes
@app.get("/registrarCliente")  
def registro_cli(req: Request):
    return template.TemplateResponse("clientes.html", {"request": req})

@app.post("/CargarCliente")
async def cargar_cli(
    req: Request,
    NombreCliente: str = Form(...),
    RUC: str = Form(...),
    direccion: str = Form(...),
    telefono: int = Form(...)
):
    data_cliente = {
        "NombreCliente": NombreCliente,
        "RUC": RUC,
        "Direccion": direccion,
        "Telefono": telefono
    }
    handle_db = HandleDB()
    cliente_registrado = handle_db.insert_cliente(data_cliente)  # Solo una vez
    del handle_db
    print(cliente_registrado)
    response = template.TemplateResponse(
        "cliente_registrado.html", {"request": req, "data_user": True, "cliente_registrado": cliente_registrado}
    )
    response.set_cookie(key="session", value="some_session_token")
    return response

@app.get("/verCliente")
def verClient(req: Request):
    handle_db = HandleDB()
    clientes = handle_db.get_cliente()
    return template.TemplateResponse("ver_clientes.html", {"request": req, "clientes": clientes})

@app.get("/EditarCliente/{IdCliente}")
def show_edit_cliente(req: Request, IdCliente: int):
    handle_db = HandleDB()
    cliente = handle_db.get_cliente_by_id(IdCliente)  # Cambiar a get_cliente_by_id para obtener un cliente específico
    del handle_db
    return template.TemplateResponse("editar_cliente.html", {"request": req, "cliente": cliente})

@app.post("/EditarCliente/{IdCliente}/update")
def update_cliente(req: Request, IdCliente: int, NombreCliente: str = Form(...), RUC: str = Form(...), Direccion: str = Form(...), Telefono: int = Form(...)):
    new_data_cliente = {
        "NombreCliente": NombreCliente,
        "RUC": RUC,
        "Direccion": Direccion,
        "Telefono": Telefono
    }
    handle_db = HandleDB()
    handle_db.update_cliente(IdCliente, new_data_cliente)  # Actualización del cliente con su ID correspondiente
    del handle_db
    return RedirectResponse(url="/verCliente", status_code=302)

@app.get("/BorrarCliente/{IdCliente}/delete")
def delete_cliente(IdCliente: int):
    handle_db = HandleDB()
    handle_db.delete_cliente(IdCliente)
    del handle_db
    return RedirectResponse(url="/verCliente", status_code=302)
#Aqui acaba toda las funcionalidades para cliente

#Desde aqui empieza todo lo referente a proveedores
@app.get("/registrarPro")
def registro_pro(req: Request):
    return template.TemplateResponse("proveedores.html", {"request": req})

@app.post("/CargarProveedor")
async def cargar_pro(
    req: Request, 
    nombrepro: str = Form(...), 
    cipro: int = Form(...), 
    rspro: str = Form(...), 
    Direccion: str = Form(...), 
    Telefono: str = Form(...)
):
    data_provee = {
        "NombreProveedor": nombrepro,
        "CIpro": cipro,
        "RUC": rspro,
        "Direccion": Direccion,
        "Telefono": Telefono
    }
    handle_db = HandleDB()
    proveedor_registrado = handle_db.insert_proveedor(data_provee) # Solo una vez
    del handle_db
    print(proveedor_registrado)
    response = template.TemplateResponse(
        "proveedor_registrado.html", {"request": req, "data_user": True, "proveedor_registrado": proveedor_registrado}
    )
    response.set_cookie(key="session", value="some_session_token")
    return response

@app.get("/verProveedor")
def verProveedor(req: Request):
    handle_db = HandleDB()
    proveedores = handle_db.get_pro()
    return template.TemplateResponse("ver_proveedores.html", {"request": req, "proveedores": proveedores})

@app.get("/EditarProvee/{IdPro}")
def show_edit_provee(req: Request, IdPro: int):
    handle_db = HandleDB()
    proveedor = handle_db.get_prove_by_id(IdPro)  # Cambiar a get_prove_by_id para obtener un proveedor específico
    del handle_db
    return template.TemplateResponse("editar_proveedor.html", {"request": req, "proveedor": proveedor})

@app.post("/EditarProvee/{IdPro}/update")
def update_prove(
    req: Request,
    IdPro: int,
    NombreProveedor: str = Form(...),
    CIpro: int = Form(...),
    RUC: str = Form(...),
    Direccion: str = Form(...),
    Telefono: str = Form(...),
):
    new_data_provee = {
        "NombreProveedor": NombreProveedor,
        "CIpro": CIpro,
        "RUC": RUC,
        "Direccion": Direccion,
        "Telefono": Telefono,
    }
    handle_db = HandleDB()
    handle_db.update_proveedor(IdPro, new_data_provee)
    del handle_db
    return RedirectResponse(url="/verProveedor", status_code=302)

@app.get("/BorrarProvee/{IdPro}/delete")
def delete_provee(IdPro: int):
    handle_db = HandleDB()
    handle_db.delete_proveedor(IdPro)
    del handle_db
    return RedirectResponse(url="/verProveedor", status_code=302)
#Aqui acaba toda las funcionalidades para proveedor

#Desde aqui empieza todo lo referente a Camiones
@app.get("/registrarCami")
def registro_camion(req: Request):
    return template.TemplateResponse("camiones.html", {"request": req})

@app.post("/CargarCami")
async def cargar_cami(
    req: Request,
    nrocami: str = Form(...),
    marcacami: str = Form(...),
    modelocami: str = Form(...),
    tipo: str = Form(...)
):
    data_camion = {
        "NroCamion": nrocami,
        "Marca": marcacami,
        "Modelo": modelocami,
        "Estado": tipo
    }
    handle_db = HandleDB()
    camion_registrado = handle_db.insert_camion(data_camion) #Solo una vez
    del handle_db
    print(camion_registrado)
    response = template.TemplateResponse(
        "camion_registrado.html", {"request": req, "data_user": True, "camion_registrado": camion_registrado}
    )
    response.set_cookie(key="session", value="some_session_token")
    return response

@app.get("/verCamion")
def verCamion(req: Request):
    handle_db = HandleDB()
    camiones = handle_db.get_cami()
    return template.TemplateResponse("ver_camiones.html", {"request": req, "camiones": camiones})

@app.get("/EditarCamion/{IdCamion}")
def show_edit_camion(req: Request, IdCamion: int):
    handle_db = HandleDB()
    camion = handle_db.get_cami_by_id(IdCamion) # Cambiar a get_cami_by_id para obtener un camion específico
    del handle_db
    return template.TemplateResponse("editar_camion.html", {"request": req, "camion": camion})

@app.post("/EditarCamion/{IdCamion}/update")
def update_cami(
    req: Request,
    IdCamion: int,
    NroCamion: str = Form(...),
    Marca: str = Form(...),
    Modelo: str = Form(...),
    Estado: str = Form(...)
):
    new_data_cami = {
        "NroCamion": NroCamion,
        "Marca": Marca,
        "Modelo": Modelo,
        "Estado": Estado
    }
    handle_db = HandleDB()
    handle_db.update_camion(IdCamion, new_data_cami)
    del handle_db
    return RedirectResponse(url="/verCamion", status_code=302)

@app.get("/BorrarCamion/{IdCamion}/delete")
def delete_camion(IdCamion: int):
    handle_db = HandleDB()
    handle_db.delete_camion(IdCamion)
    del handle_db
    return RedirectResponse(url="/verCamion", status_code=302)
#Aqui acaba toda las funcionalidades para camion

#Aqui empieza la funcionalidad relacionada con las Actividades
#Las funcionalidades para hacer los pedidos
@app.get("/PedidosPro")
def pedidosProv(req: Request):
    handle_db = HandleDB()
    # Obtener nombres de proveedores desde la base de datos
    nombres_proveedores = handle_db.get_nombres_proveedores()
    return template.TemplateResponse("pedidos.html", {"request": req, "nombres_proveedores": nombres_proveedores})

@app.post("/CargarPedido")
def cargarpedido(
    req: Request, 
    nombrepro: str = Form(...), 
    pedido_mat: str = Form(...), 
    formapago: str = Form(...)
):
    data_pedido = {
        "NombrePro": nombrepro,
        "DescripPedido": pedido_mat,
        "FormaPago": formapago
    }
    handle_db = HandleDB()
    pedido_registrado = handle_db.insert_pedido(data_pedido)
    if pedido_registrado:
        return template.TemplateResponse(
            "pedido_registrado.html", {"request": req, "data_user": True, "pedido_registrado": pedido_registrado}
        )

@app.get("/verPedidos")
def verPedido(req: Request):
    handle_db = HandleDB()
    pedidos = handle_db.get_pedidos()
    return template.TemplateResponse("ver_pedidos.html", {"request": req, "pedidos": pedidos})

@app.get("/EditarPedido/{IdPedido}")
def show_edit_pedido(req: Request, IdPedido: int):
    handle_db = HandleDB()
    pedido = handle_db.get_pedido_by_id(IdPedido) # Cambiar a get_pedido_by_id para obtener un pedido específico
    del handle_db
    return template.TemplateResponse("editar_pedido.html", {"request": req, "pedido": pedido})

@app.post("/EditarPedido/{IdPedido}/update")
def update_pedido(
    req: Request,
    IdPedido: int,
    DescripPedido: str = Form(...),
    formapago: str = Form(...)
):
    new_data_pedido = {
        "DescripPedido": DescripPedido,
        "FormaPago": formapago
    }
    handle_db = HandleDB()
    handle_db.update_pedido(IdPedido, new_data_pedido)
    del handle_db
    return RedirectResponse(url="/verPedidos", status_code=302)

@app.get("/BorrarPedido/{IdPedido}/delete")
def delete_pedido(IdPedido: int):
    handle_db = HandleDB()
    handle_db.delete_pedido(IdPedido)
    del handle_db
    return RedirectResponse(url="/verPedidos", status_code=302)
#Aqui terminan las funcionalidades para hacer los pedidos

#Las funcionalidades para hacer las compras a proveedores inician aqui
@app.get("/ComprasPro")
def ComprasProv(req: Request):
    handle_db = HandleDB()
    # Obtener nombres de proveedores desde la base de datos
    nombres_proveedores = handle_db.get_nombres_proveedores()
    # Obtener nombres y precios de materiales
    nombres_materiales_con_precio = handle_db.get_nombres_materiales_con_precio()
    return template.TemplateResponse("compras.html", {"request": req, "nombres_proveedores": nombres_proveedores, "nombres_materiales_con_precio": nombres_materiales_con_precio})

@app.post("/ImprimirCompra")
def ImprimirCompra(
    req: Request,
    nombrepro: str = Form(...),
    nombremat: str = Form(...),
    descripcion: str = Form(...)
):
    data_compra = {
        "Proveedor": nombrepro,
        "DetalleCompra": nombremat,
        "DescripCompra": descripcion
    }
    handle_db = HandleDB()
    compra_imprimida = handle_db.insert_compra(data_compra)
    if compra_imprimida:
        return template.TemplateResponse("ticket_compra.html", {"request": req, "data_user": True, "compra_imprimida": compra_imprimida})

@app.get("/verCompras")
def verCompras(req: Request):
    handle_db = HandleDB()
    compras = handle_db.get_compras()
    return template.TemplateResponse("ver_ticket.html", {"request": req, "compras": compras})

@app.get("/BorrarCompra/{IdCompra}/delete")
def delete_compra(IdCompra: int):
    handle_db = HandleDB()
    handle_db.delete_compra(IdCompra)
    del handle_db
    return RedirectResponse(url="/verCompras", status_code=302)
#Aqui terminan las funcionalidades para hacer las compras

#Las funcionalidades para hacer los pagos a proveedores inician aqui
@app.get("/PagosPro")
def PagosProv(req: Request):
    handle_db = HandleDB()
    # Obtener nombres de proveedores desde la base de datos
    nombres_proveedores = handle_db.get_nombres_proveedores()
    return template.TemplateResponse("pagos.html", {"request": req, "nombres_proveedores": nombres_proveedores})

@app.post("/procesar_pago")
async def procesar_pago(
    req: Request,
    nombrepro: str = Form(...),
    monto: float = Form(...),
    forma_pago: str = Form(...),  # Este campo es para la forma de pago
):
    # Lógica para procesar el pago en la base de datos
    data_pago = {
        "Proveedor": nombrepro,
        "Monto": monto,
        "FormaPago": forma_pago,
    }
    handle_db = HandleDB()
    proceso_pago = handle_db.insert_pago(data_pago)
    if proceso_pago:
        return template.TemplateResponse("pago_hecho.html", {"request": req, "data_user": True, "proceso_pago": proceso_pago})

@app.get("/verOrden")
def verOrden(req: Request):
    handle_db = HandleDB()
    orden = handle_db.get_pagos()
    return template.TemplateResponse("pagos_realizados.html", {"request": req, "orden": orden})
#Aqui acaba todas las funcionalidades para los pagos
#Aqui termina la funcionalidad relacionada con las Actividades







