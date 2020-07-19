from django.http import QueryDict
import re 

from src.libs.validations import *
from src.entities.class_ import Class
from src.dao.class_ import ClassDAO


class ClassModel:

    def register(self, args:QueryDict = None):
        class_ = None
        
        # 1º Pegando os parâmetros de interesse
        try:
            class_ = Class(args.get('classname', '').strip(), args.get('title', '').strip(), args.get('description', '').strip(),
            None, 1, args.get('max_members', '').strip(), args.get('situation', '').strip())
        except:
            raise Exception('invalid arguments.')
        
        # 2º Validando inputs
        # @TODO: Checar se classname ja existe ou se existe um username igual a classname
        if (class_.classname == '') or (len(class_.classname) < 2) or (not is_classname(class_.classname)):
            raise Exception('invalid classname parameter')
        if class_.title == '':
            raise Exception('invalid title parameter')
        if (not is_integer(class_.max_members)) or (int(class_.max_members) < 0) or (int(class_.max_members) > 50):
            raise Exception('invalid max number of members parameter')

        # 3º Realizando o registro
        try:
            ClassDAO().insert(class_)
        except Exception as e:
            raise e

        return None
    
    def update(self, args:QueryDict = None):
        # 1º Extraindo parâmetros de interesse
        try: 
            class_ = Class(args.get('classname', '').strip(), args.get('title', '').strip(), args.get('description', '').strip(),
            None, args.get('members_qtt', ''), args.get('max_members', '').strip(), args.get('situation', '').strip())
        except Exception as e:
            print('[ClassModel.update]', str(e))
            raise Exception('invalid arguments.')
        
        # 2º Validando os parâmetros
        if (class_.classname == '') or (len(class_.classname) < 2) or (not is_classname(class_.classname)):
            raise Exception('invalid classname parameter')
        if class_.title == '':
            raise Exception('invalid title parameter')
        if (not is_integer(class_.max_members)) or (int(class_.max_members) < 0) or (int(class_.max_members) > 50) or int(class_.max_members < class_.members_qtt):
            raise Exception('invalid max number of members parameter')
        
        # 3º Atualizando a tabela
        try:
            rows_affected = ClassDAO().update(class_)
            if rows_affected != 1:
                raise Exception('class not found. Please check if the classname param is valid!')
        except Exception as e:
            raise e

    def search(self, args:QueryDict = None):
        class_ = None

        # 1º Extraindo parâmetros de interesse
        try: 
            class_ = Class(classname = args.get('classname', '').strip())
        except Exception as e:
            print('[ClassModel.search]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando os parâmetros    
        if (class_.classname == '') or (len(class_.classname) < 2) or (not is_classname(class_.classname)):
            raise Exception('invalid classname parameter')

        # 3º Buscando a turma
        try:
            class_ = ClassDAO().select(class_)
            if class_ is None:
                raise Exception('could not find class by classname.')
        except Exception as e:
            raise e

        return dict(class_)

    def get_classes(self, args:QueryDict = None):
        n_rows = 0
        classes = []
        classes_dict = []

        try:
            n_rows, classes = ClassDAO().get_classes(args.get('username', '').strip(), args.get('situation', '').strip())
        except Exception as e:
            print('[classModel.search]', str(e))
            raise Exception('invalid arguments.')

        for c in classes:
            dict_c = {
                'username':c[0],
                'title':c[1],
                'description':c[2],
                'members quantity':c[3],
                'max members':c[4],
                'situation':c[5],
                'is leader':c[6],
            }
            classes_dict.append(dict_c)

        return n_rows, classes_dict