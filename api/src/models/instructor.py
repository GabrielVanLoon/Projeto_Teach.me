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

    def get_instructors(self, args:QueryDict = None):
        n_rows = 0
        instructors = []
        instructors_dict = []

        # 1º Extraindo parâmetros de interesse

        max_price = args.get('max_price', '').strip()
        max_price = float(max_price) if (is_numeric(max_price)) else ''

        try: 
            n_rows, instructors = InstructorDAO().get_instructors(args.get('subject', '').strip(), args.get('city', '').strip(), 
                            args.get('state', '').strip(), args.get('weekday', '').strip(), args.get('time', '').strip(), max_price)
        except Exception as e:
            print('[instructorModel.search]', str(e))
            raise Exception('invalid arguments.')

        for r in instructors:
            dict_r = {
                'username':r[0],
                'name':r[1],
                'last_name':r[2],
                'degree': r[3],
                'abstract':r[4],
                'subject':args.get('subject', '').strip(),
                'base_price':r[6],
            }
            instructors_dict.append(dict_r)

        return n_rows, instructors_dict