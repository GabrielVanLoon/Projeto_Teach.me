import re 

from src.entities.user import User
from src.dao.user import UserDAO

class UserModel:

    def register(self, args = None):
        user = None

        # 1º Pegando os parâmetros de interesse
        try: 
            user = User(args.get('username', '').strip(), args.get('email', '').strip(), args.get('password', '').strip(), 
                args.get('name', '').strip(), args.get('last_name', '').strip(), None, False)
        except Exception as e:
            print('[userModel.register]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando inputs
        if (user.username == '') or (len(user.username) < 2):
            raise Exception('invalid username field.')
        if not re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', user.email):
            raise Exception('invalid email field.')
        if (user.password == '') or (len(user.password) < 8):
            raise Exception('invalid password field.')
        if (user.name == '') or (user.last_name == ''):
            raise Exception('invalid name and last name fields')

        # 3º Realizando o registro
        try:
            UserDAO().insert(user)
        except Exception as e:
            raise e

        return None

    def update(self, args = {}):
        return None

    def search(self, args = {}):
        return None