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

@app.post("/user", response_class=HTMLResponse)
def user(req: Request, username: str = Form(), password: str = Form()):
        verify = check_user(username, password)
        if verify:
            return template.TemplateResponse(
                "employd.html", {"request": req, "data_user": verify}
            )


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

@app.get("/registrarMat")
def registro_mat(req: Request):
    return template.TemplateResponse("materiales.html", {"request": req})


@app.post("/CargarM")
def cargar_mat(
    req: Request,
    nombrematerial: str = Form(...),
    desc: str = Form(...),
    precio: float = Form(...),
    cantidad: int = Form(...)
):
    data_mat = {
        "NombreMaterial": nombrematerial,
        "DescripcionMat": desc,
        "Precio": precio,
        "Cantidad": cantidad
    }
    handle_db = HandleDB()
    handle_db.insert_mat(data_mat)
    del handle_db
    return template.TemplateResponse("employd.html", {"request": req, "data_user": True})  #Comando para volver al menu del empleado

@app.get("/verMat")
def verMat(req: Request):
    handle_db = HandleDB()
    materiales = handle_db.get_all_mat()
    print(materiales)
    return template.TemplateResponse("ver_materiales.html", {"request": req, "materiales": materiales})


@app.get("/EditarM/{id_del_material}")
def edit_mat(
    req: Request,
    id_del_material: int,
    nombrematerial: str = Form(...),
    desc: str = Form(...),
    precio: float = Form(...),
    cantidad: int = Form(...)
):
    n_data_mat = {
        "id": id_del_material,
        "NombreMaterial": nombrematerial,
        "DescripcionMat": desc,
        "Precio": precio,
        "Cantidad": cantidad
    }
    handle_db = HandleDB()
    handle_db.update_mat(n_data_mat)
    del handle_db
    return RedirectResponse(url="/verMat", status_code=302)

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

    mensaje = ""
    if cliente_registrado:
        mensaje = "Un nuevo cliente ha sido registrado con éxito"
    else:
        mensaje = "El cliente ya existe. Por favor, registre un nuevo cliente"

    return template.TemplateResponse(
        "employd.html", {"request": req, "data_user": True, "mensaje": mensaje}
    )


@app.get("/verCliente")
def verClient(req: Request):
    handle_db = HandleDB()
    clientes = handle_db.get_cliente()
    return template.TemplateResponse("ver_clientes.html", {"request": req, "clientes": clientes})

@app.get("/EditarCliente/{id_del_cliente}")
def show_edit_cliente(req: Request, id_del_cliente: int):
    handle_db = HandleDB()
    cliente = handle_db.get_cliente_by_id(id_del_cliente)  # Cambiar a get_cliente_by_id para obtener un cliente específico
    del handle_db
    return template.TemplateResponse("editar_cliente.html", {"request": req, "cliente": cliente})

@app.post("/EditarCliente/{id_del_cliente}/update")
def update_client(req: Request, id_del_cliente: int, NombreCliente: str = Form(...), RUC: str = Form(...), direccion: str = Form(...), telefono: int = Form(...)):
    # Procesar la actualización del cliente
    new_data_cliente = {
        "id_del_cliente": id_del_cliente,
        "NombreCliente": NombreCliente,
        "RUC": RUC,
        "Direccion": direccion,
        "Telefono": telefono
    }
    handle_db = HandleDB()
    handle_db.update_cliente(new_data_cliente)
    del handle_db
    return RedirectResponse(url="/verCliente", status_code=302)


@app.get("/registrarPro")
def registro_cli(req: Request):
    return template.TemplateResponse("proveedores.html", {"request": req})

