from model.handle_db import HandleDB
from werkzeug.security import check_password_hash

class IncorrectPasswordError(Exception):
    pass

def check_user(username, passw):
    user = HandleDB()
    filter_user = user.get_only(username)
    
    if filter_user:
        same_passw = check_password_hash(filter_user[4], passw)
        if same_passw:
            list_tareas = user.get_all()
            return list_tareas
        else:
            raise IncorrectPasswordError("Contraseña incorrecta")
    else:
        raise ValueError("Usuario no encontrado")
try:
    result = check_user("nombre_de_usuario", "contraseña_incorrecta")
    # Hacer algo con el resultado
except IncorrectPasswordError:
    print("Contraseña incorrecta. Por favor, inténtalo de nuevo.")
except ValueError:
    print("Usuario no encontrado. Por favor, regístrate.")


