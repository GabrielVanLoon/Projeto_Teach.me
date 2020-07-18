from django.http import QueryDict
import re 

from src.libs.validations import *
from src.entities.user import User
from src.entities.class_ import Class 
from src.dao.user import UserDAO
from src.dao.class_ import ClassDAO

class UserModel:

    def register(self, args:QueryDict = None):
        user = None

        # 1º Pegando os parâmetros de interesse
        try: 
            user = User(args.get('username', '').strip(), args.get('email', '').strip(), args.get('password', '').strip(), 
                            args.get('name', '').strip(), args.get('last_name', '').strip(), None, False)
        except Exception as e:
            print('[userModel.register]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando inputs        
        if (user.username == '') or (len(user.username) < 2) or (not is_username(user.username)):
            raise Exception('invalid username parameter.')
        if not is_valid_mail(user.email):
            raise Exception('invalid email parameter.')
        if (user.password == '') or (len(user.password) < 8):
            raise Exception('invalid password parameter.')
        if (not is_alphabetic(user.name, with_spaces=True)) or (not is_alphabetic(user.last_name, with_spaces=True)):
            raise Exception('invalid name and last name parameters')
        
        # 3º Realizando o registro
        try:
            UserDAO().insert(user)
        except Exception as e:
            raise e
        
        # 4º Se registrou como usuário, então pode registrar como turma particular
        temp_class = Class(user.username, '', '', '', 1, 1, 'PARTICULAR')
        try:
            ClassDAO().insert(temp_class)
        except Exception as e:
            raise e

        return None

    def update(self, args:QueryDict = None):
        # 1º Extraindo parâmetros de interesse
        try: 
            user = User(args.get('username', '').strip(), args.get('email', '').strip(), None, 
                            args.get('name', '').strip(), args.get('last_name', '').strip(), None, False)
        except Exception as e:
            print('[userModel.update]', str(e))
            raise Exception('invalid arguments.')
        
        # 2º Validando os parâmetros    
        if (user.username == '') or (len(user.username) < 2) or (not is_username(user.username)):
            raise Exception('invalid username parameter.')
        if not is_valid_mail(user.email):
            raise Exception('invalid email parameter.')
        if (not is_alphabetic(user.name, with_spaces=True)) or (not is_alphabetic(user.last_name, with_spaces=True)):
            raise Exception('invalid name and last name parameters')
        
        # 3º Atualizando a tabela
        try:
            rows_affected = UserDAO().update(user)
            if rows_affected != 1:
                raise Exception('user not found. Please check if the username param is valid!')
        except Exception as e:
            raise e

    def search(self, args:QueryDict = None):
        user = None

        # 1º Extraindo parâmetros de interesse
        try: 
            user = User(username = args.get('username', '').strip())
        except Exception as e:
            print('[userModel.search]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando os parâmetros    
        if (user.username == '') or (len(user.username) < 2) or (not is_username(user.username)):
            raise Exception('invalid username parameter.')

        # 3º Buscando o usuario
        try:
            user = UserDAO().select(user)
            if user is None:
                raise Exception('couldn\'t  not find user by username.')
        except Exception as e:
            raise e

        return dict(user)

    def check_username(self, args:QueryDict = None):
        user = None

        # 1º Extraindo parâmetros de interesse
        try: 
            user = User(username = args.get('username', '').strip())
        except Exception as e:
            print('[userModel.search]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando os parâmetros    
        if (user.username == '') or (len(user.username) < 2) or (not is_username(user.username)):
            raise Exception('invalid username parameter.')

        # 3º Buscando o usuario
        temp_class = Class(user.username)
        try:
            return_user  = UserDAO().select(user)
            return_class = ClassDAO().select(temp_class) 

            if (return_user is not None) or (return_class is not None):
                raise Exception('username already in use.')
        except Exception as e:
            raise e
