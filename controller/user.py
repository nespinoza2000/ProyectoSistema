from model.handle_db import HandleDB
from werkzeug.security import generate_password_hash

#The bcrypt utilizar


class User:
    def __init__(self, data_user):
        self.db = HandleDB()
        self.data_user = data_user

    def create_user(self):
        self._add_id()
        self._passw_encrypt()
        self.db.insert(self.data_user)

    def _add_id(self):
        users = self.db.get_all()
        if users:
            last_user = users[-1]
            id_user = int(last_user[0])
            self.data_user["id"] = str(id_user + 1)
        else:
            self.data_user["id"] = "1"

    def _passw_encrypt(self):
        self.data_user["password"] = generate_password_hash(self.data_user["password"], method="pbkdf2:sha256", salt_length=8)
