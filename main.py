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

@app.get("/registrarCliente")  
def registro_cli(req: Request):
    return template.TemplateResponse("clientes.html", {"request": req})

@app.post("/CargarCliente")
async def cargar_cli(
    req: Request,
    NombreCliente: str = Form(...),
    RUC: str = Form(...)  # Asegúrate de que estos campos coincidan con el formulario HTML
):
    data_cliente = {
        "NombreCliente": NombreCliente,
        "RUC": RUC
    }
    handle_db = HandleDB()
    handle_db.insert_cliente(data_cliente)
    del handle_db
    return template.TemplateResponse(
        "employd.html", {"request": req, "data_user": True})

@app.get("/verCliente")
def verClient(req: Request):
    handle_db = HandleDB()
    clientes = handle_db.get_cliente()
    return template.TemplateResponse("ver_clientes.html", {"request": req, "clientes": clientes})

@app.get("/registrarPro")
def registro_cli(req: Request):
    return template.TemplateResponse("proveedores.html", {"request": req})