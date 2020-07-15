from django.http import QueryDict
import re 

from src.libs.validations import is_username, is_alphanumeric, is_numeric
from src.entities.instructor import Instructor
from src.dao.instructor import InstructorDAO

class InstructorModel:

    def register(self, args:QueryDict = None):
        instructor = None

        # 1º Pegando os parâmetros de interesse
        try: 
            instructor = Instructor(args.get('username', '').strip(), args.get('abstract', '').strip(), 
                            args.get('about_me', '').strip(), args.get('degree', '').strip())
        except Exception as e:
            print('[instructorModel.register]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando inputs 
        if (not is_username(instructor.username)):
            raise Exception('invalid username parameter.')

        # 3º Realizando o registro
        try:
            InstructorDAO().insert(instructor)
        except Exception as e:
            raise e


    def update(self, args:QueryDict = None):
        # 1º Extraindo parâmetros de interesse
        try:
            instructor = Instructor(args.get('username', '').strip(), args.get('abstract', '').strip(), 
                            args.get('about_me', '').strip(), args.get('degree', '').strip())
        except Exception as e:
            print('[instructorModel.update]', str(e))
            raise Exception('invalid arguments.')
        
        # 2º Validando inputs        
        if (not is_username(instructor.username)):
            raise Exception('invalid username parameter.')

        # 3º Atualizando a tabela
        try:
            rows_affected = InstructorDAO().update(instructor)
            if rows_affected != 1:
                raise Exception('instructor not found. Please check if the username parameter is valid!')
        except Exception as e:
            raise e

    def search(self, args:QueryDict = None):
        instructor = None

        # 1º Extraindo parâmetros de interesse
        try: 
            instructor = Instructor(args.get('username', '').strip())
        except Exception as e:
            print('[instructorModel.search]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando inputs        
        if (not is_username(instructor.username)):
            raise Exception('invalid username parameter.')

        # 3º Buscando o usuario
        try:
            instructor = InstructorDAO().select(instructor)
            if instructor is None:
                raise Exception('couldn\'t  not find instructor.')
        except Exception as e:
            raise e

        return dict(instructor)