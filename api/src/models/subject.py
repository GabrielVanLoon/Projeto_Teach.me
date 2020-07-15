from django.http import QueryDict
import re 

from src.libs.validations import *
from src.entities.subject import Subject
from src.dao.subject import Subject


class SubjectModel:

    def register(self, args:QueryDict = None):
        subject = None
        
        # 1º Pegando os parâmetros de interesse
        try:
            subject = Subject(args.get('name', '').strip(), args.get('parent_subject', '').strip()
        except:
            raise Exception('invalid arguments.')
        
        # 2º Validando inputs
        # @TODO: Checar se name de Matéria ja existe
        if (subject.name == '') or (len(subject.name) < 2):
            raise Exception('invalid name parameter')
        # @TODO: Checar se parent_subject existe como name de materia

        # 3º Realizando o registro
        try:
            SubjectDAO().insert(subject)
        except Exception as e:
            raise e

        return None
    
    def update(self, args:QueryDict = None):
        # 1º Extraindo parâmetros de interesse
        try: 
            subject = Subject(args.get('name', '').strip(), args.get('parent_subject', '').strip())
        except Exception as e:
            print('[subjectModel.update]', str(e))
            raise Exception('invalid arguments.')
        
        # 2º Validando os parâmetros
        # @TODO: Checar se name de Matéria ja existe
        if (subject.name == '') or (len(subject.name) < 2):
            raise Exception('invalid name parameter')
        # @TODO: Checar se parent_subject existe como name de materia

        
        # 3º Atualizando a tabela
        try:
            rows_affected = SubjectDAO().update(subject)
            if rows_affected != 1:
                raise Exception('subject not found. Please check if the name param is valid!')
        except Exception as e:
            raise e

    def search(self, args:QueryDict = None):
        subject = None

        # 1º Extraindo parâmetros de interesse
        try: 
            subject = Subject(name = args.get('name', '').strip())
        except Exception as e:
            print('[subjectModel.search]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando os parâmetros    
         if (subject.name == '') or (len(subject.name) < 2):
            raise Exception('invalid name parameter')

        # 3º Buscando a materia
        try:
            subject = SubjectDAO().select(subject)
            if subject is None:
                raise Exception('could not find subject by name.')
        except Exception as e:
            raise e

        return dict(subject)