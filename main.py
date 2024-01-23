from pstats import Stats
from fastapi import FastAPI, HTTPException, Request, Response, Form
from fastapi.params import Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from controller.user import User
from lib.check_passw import check_user
from model.handle_db import HandleDB
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime

app = FastAPI()

template = Jinja2Templates(directory="./view")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/", response_class=HTMLResponse)
def root(req: Request):
    return template.TemplateResponse("index.html", {"request": req})

@app.post("/", response_class=HTMLResponse)
def root(req: Request):
    return template.TemplateResponse("index.html", {"request": req})

@app.get("/signup", response_class=HTMLResponse)
def signup(req: Request):
    return template.TemplateResponse("signup.html", {"request": req})

@app.get("/favicon.ico") #Para ignorar el mensaje de error cuando se carga un icono por defecto
async def get_favicon():
    raise HTTPException(status_code=404, detail="Favicon not found")

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
    domicilio: str = Form(...),
    telefono: int = Form(...),
    email: str = Form(...)
):
    data_cliente = {
        "NombreCliente": NombreCliente,
        "RUC": RUC,
        "Direccion": direccion,
        "Domicilio": domicilio,
        "Telefono": telefono,
        "Email": email
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
def update_cliente(req: Request, IdCliente: int, NombreCliente: str = Form(...), RUC: str = Form(...), Direccion: str = Form(...), Domicilio: str = Form(...), Telefono: int = Form(...), Email: str = Form(...)):
    new_data_cliente = {
        "NombreCliente": NombreCliente,
        "RUC": RUC,
        "Direccion": Direccion,
        "Domicilio": Domicilio,
        "Telefono": Telefono,
        "Email": Email
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
    rspro: str = Form(...), 
    Direccion: str = Form(...),
    Domicilio: str = Form(...),
    Telefono: str = Form(...),
    Email: str = Form(...)
):
    data_provee = {
        "NombreProveedor": nombrepro,
        "RUC": rspro,
        "Direccion": Direccion,
        "Domicilio": Domicilio,
        "Telefono": Telefono,
        "Email": Email
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
    RUC: str = Form(...),
    Direccion: str = Form(...),
    Domicilio: str = Form(...),
    Telefono: int = Form(...),
    Email: str = Form(...)
):
    new_data_provee = {
        "NombreProveedor": NombreProveedor,
        "RUC": RUC,
        "Direccion": Direccion,
        "Domicilio": Domicilio,
        "Telefono": Telefono,
        "Email": Email
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
    nrochasis: str = Form(...),
    chapa: str = Form(...),
    tipo: str = Form(...)
):
    data_camion = {
        "NroCamion": nrocami,
        "Marca": marcacami,
        "Modelo": modelocami,
        "Chasis": nrochasis,
        "Chapa": chapa,
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
    Chasis: str = Form(...),
    Chapa: str = Form(...),
    Estado: str = Form(...)
):
    new_data_cami = {
        "NroCamion": NroCamion,
        "Marca": Marca,
        "Modelo": Modelo,
        "Chasis": Chasis,
        "Chapa": Chapa,
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
    nombremat: str = Form(...),
    cantidad: int = Form(...),
    caracteristicas: str = Form(...),
    formapago: str = Form(...)
):
    data_pedido = {
        "NombrePro": nombrepro,
        "NombreMat": nombremat,
        "Cantidad": cantidad,
        "Caracteristicas": caracteristicas,
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
    NombreMat: str = Form(...),
    Cantidad: int = Form(...),
    Caracteristicas: str = Form(...),
    formapago: str = Form(...)
):
    new_data_pedido = {
        "NombreMat": NombreMat,
        "Cantidad": Cantidad,
        "Caracteristicas": Caracteristicas,
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
    return template.TemplateResponse("compras.html", {"request": req, "nombres_proveedores": nombres_proveedores})

@app.post("/ImprimirCompra")
def ImprimirCompra(
    req: Request,
    nombrepro: str = Form(...),
    material: str = Form(...),
    descripcion: str = Form(...),
    detalle: str = Form(...),
    formapago: str = Form(...)
):
    data_compra = {
        "Proveedor": nombrepro,
        "Material": material,
        "Descripcion": descripcion,
        "Detalle": detalle,
        "Pago": formapago
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
    actividad: str = Form(...),
    monto: int = Form(...),
    forma_pago: str = Form(...),  # Este campo es para la forma de pago
):
    # Lógica para procesar el pago en la base de datos
    data_pago = {
        "Proveedor": nombrepro,
        "Actividad": actividad,
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

#Aqui empieza toda funcionalidad con las tareas
@app.get("/AdminTareas")
def RealizarTareas(req: Request):
    return template.TemplateResponse("tareas.html", {"request": req})

@app.post("/CargarTarea")
async def cargar_tarea(
    req: Request,
    tarea: str = Form(...),
    detalle: str = Form(...)
):
    data_tarea = {
        "Tarea": tarea,
        "Detalles": detalle
    }
    handle_db = HandleDB()
    tarea_registrada = handle_db.insert_tarea(data_tarea) #Solo una vez
    del handle_db
    response = template.TemplateResponse("tarea_registrada.html", {"request": req, "data_user": True, "tarea_registrada": tarea_registrada})
    response.set_cookie(key="session", value="some_session_token")
    return response

@app.get("/verTarea")
def verTarea(req: Request):
    handle_db = HandleDB()
    tareas = handle_db.get_tareas()
    return template.TemplateResponse("ver_tareas.html", {"request": req, "tareas": tareas})

@app.get("/EditarTarea/{IdTarea}")
def mostrar_edit_tarea(req: Request, IdTarea: int):
    handle_db = HandleDB()
    tarea = handle_db.get_tarea_by_id(IdTarea) # Cambiar a get_tarea_by_id para obtener una tarea específico
    del handle_db
    return template.TemplateResponse("editar_tarea.html", {"request": req, "tarea": tarea})

@app.post("/EditarTarea{IdTarea}/update")
def update_tarea(
    req: Request,
    IdTarea: int,
    Tarea: str = Form(...),
    Detalles: str = Form(...)
):
    new_data_tarea = {
        "Tarea": Tarea,
        "Detalles": Detalles
    }
    handle_db = HandleDB()
    handle_db.update_tarea(IdTarea, new_data_tarea)
    del handle_db
    return RedirectResponse(url="/verTarea", status_code=302)

@app.get("/BorrarTarea/{IdTarea}/delete")
def delete_tarea(IdTarea: int):
    handle_db = HandleDB()
    handle_db.delete_tarea(IdTarea)
    del handle_db
    return RedirectResponse(url="/verTarea", status_code=302)
#Aqui acaban todas las funcionalidades para administrar tareas

#Aqui inicia la funcionalidad de hacer un venta para los clientes
@app.get("/VentaCli")
def VentaCli(req: Request):
    handle_db = HandleDB()
    # Obtener nombres de los clientes desde la base de datos
    nombres_clientes = handle_db.get_name_cliente()
    # Obtener nombres y descripciones de materiales
    nom_mat_desc = handle_db.get_name_mat_desc()
    # Obtener los precios de los materiales
    nom_mat_pre = handle_db.get_name_mat_pre()
    # Obtener las cantidades de los materiales
    return template.TemplateResponse("ventas.html", {"request": req, "nombres_clientes": nombres_clientes, "nom_mat_desc": nom_mat_desc, "nom_mat_pre": nom_mat_pre})

@app.post("/ProcesarVenta")
def processing_sell(
    req: Request,
    NombreCliente: str = Form(...),
    nombremat: str = Form(...),
    cantidad: str = Form(...),
    precio: int = Form(...),
    forma_pago_v: str = Form(...)
):
    data_venta = {
        "Cliente": NombreCliente,
        "Material": nombremat,
        "Cantidad": cantidad,
        "Precio": precio,
        "FormaPago": forma_pago_v
    }
    handle_db = HandleDB()
    try:
        proceso_venta = handle_db.insert_ventas(data_venta)
        if proceso_venta:
            return template.TemplateResponse("venta_exitosa.html", {"request": req, "data_user": True, "proceso_venta": proceso_venta})
    except Exception as e:
        print(f"Error en el procesamiento de la venta: {e}")

@app.get("/verVenta")
def verVenta(req: Request):
    handle_db = HandleDB()
    ventas = handle_db.get_ventas()
    return template.TemplateResponse("ver_ventas.html", {"request": req, "ventas": ventas})

@app.get("/ImprimirFactura/{id_venta}")
def imprimir_factura(req: Request, id_venta: int):
    handle_db = HandleDB()
    factura_html = handle_db.generar_factura(id_venta)
    # Devolver el contenido HTML de la factura
    return HTMLResponse(content=factura_html, status_code=200)

@app.get("/BorrarVenta/{IdVenta}/delete")
def delete_venta(IdVenta: int):
    handle_db = HandleDB()
    handle_db.delete_venta(IdVenta)
    del handle_db
    return RedirectResponse(url="/verVenta", status_code=302)
#Aqui terminan las funcionalidad para hacer las ventas

#Aqui empiezan la funcionalidad relacionada sobre el manejo financiero
#Las funcionalidades de ingresos empiezan aqui
@app.get("/Menu")
def menu_ineg(req: Request): #Nota al margen ineg es de Ingreso y Egreso
    return template.TemplateResponse("menu.html", {"request": req})

@app.post("/Calculo")
def calculation(
    req: Request,
    Capital: int = Form(...),
    Activo: int = Form(...),
    Pasivo: int = Form(...)
):
    data_ineg = {
        "Capital": Capital,
        "Activo": Activo,
        "Pasivo": Pasivo
    }
    handle_db = HandleDB()
    financiera_ineg = handle_db.insert_calc(data_ineg) #Solo una vez
    del handle_db
    response = template.TemplateResponse("menu_registrado.html", {"request": req, "data_user": True, "financiera_ineg": financiera_ineg})
    response.set_cookie(key="session", value="some_session_token")
    return response

@app.get("/verFinanzas")
def showBalance(req: Request):
    handle_db = HandleDB()
    finanzas = handle_db.get_financiera()
    return template.TemplateResponse("ver_menu.html", {"request": req, "finanzas": finanzas})

@app.get("/BorrarFinanza/{IdFinanza}/delete")
def delete_finanza(IdFinanza: int):
    handle_db = HandleDB()
    handle_db.delete_finanza(IdFinanza)
    del handle_db
    return RedirectResponse(url="/verFinanzas", status_code=302)
