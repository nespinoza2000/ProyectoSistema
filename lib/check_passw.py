from model.handle_db import HandleDB
from werkzeug.security import check_password_hash


def check_user(username, passw):
    user = HandleDB()
    filter_user = user.get_only(username)
    if filter_user:
        same_passw = check_password_hash(filter_user[4], passw)
        if same_passw:
            list_tareas = user.get_all()
            return list_tareas
        else:
            return ValueError
