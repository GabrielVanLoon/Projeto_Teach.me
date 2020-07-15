from django.http import QueryDict
import re 

from src.libs.validations import *
from src.entities.member_rating import MemberRating
from src.dao.member_rating import MemberRatingDAO

class MemberRatingModel:

    def register(self, args:QueryDict = None):
        member_rating = None

        # 1º Pegando os parâmetros de interesse
        try: 
            member_rating = MemberRating(args.get('student', '').strip(), args.get('classname', '').strip(), 
                args.get('proposal', '').strip(), args.get('lesson_number', '').strip(), args.get('rate', '').strip())
        except Exception as e:
            print('[memberRatingModel.register]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando inputs 
        if (not is_username(member_rating.student)):
            raise Exception('invalid student parameter.')
        if (not is_classname(member_rating.classname)):
            raise Exception('invalid classname parameter.')
        if (not is_alphanumeric(member_rating.proposal)):
            raise Exception('invalid proposal parameter.')
        if (not is_integer(member_rating.proposal)):   
            raise Exception('invalid lesson number parameter.')
        if (not is_integer(member_rating.rate)): 
            raise Exception('invalid rate parameter.')
        
        member_rating.rate = int( member_rating.rate)
        if member_rating.rate > 5 or member_rating.rate < 1: 
            raise Exception('invalid rate parameter. The value must be betwen 1 and 5.')
        
        # 3º Realizando o registro
        try:
            MemberRatingDAO().insert(member_rating)
        except Exception as e:
            raise e


    def update(self, args:QueryDict = None):
        # 1º Extraindo parâmetros de interesse
        try:
            member_rating = MemberRating(args.get('student', '').strip(), args.get('classname', '').strip(), 
                args.get('proposal', '').strip(), args.get('lesson_number', '').strip(), args.get('rate', '').strip())
        except Exception as e:
            print('[memberRatingModel.update]', str(e))
            raise Exception('invalid arguments.')
        
        # 2º Validando inputs 
        if (not is_username(member_rating.student)):
            raise Exception('invalid student parameter.')
        if (not is_classname(member_rating.classname)):
            raise Exception('invalid classname parameter.')
        if (not is_alphanumeric(member_rating.proposal)):
            raise Exception('invalid proposal parameter.')
        if (not is_integer(member_rating.proposal)):   
            raise Exception('invalid lesson number parameter.')
        if (not is_integer(member_rating.rate)): 
            raise Exception('invalid rate parameter.')
        
        member_rating.rate = int( member_rating.rate)
        if member_rating.rate > 5 or member_rating.rate < 1: 
            raise Exception('invalid rate parameter. The value must be betwen 1 and 5.')

        # 3º Atualizando a tabela
        try:
            rows_affected = MemberRatingDAO().update(member_rating)
            if rows_affected != 1:
                raise Exception('member rating not found. Please check if the params are valid!')
        except Exception as e:
            raise e

    def search(self, args:QueryDict = None):
        member_rating = None

        # 1º Extraindo parâmetros de interesse
        try: 
             member_rating = MemberRating(args.get('student', '').strip(), args.get('classname', '').strip(), 
                args.get('proposal', '').strip(), args.get('lesson_number', '').strip(), args.get('rate', '').strip())
        except Exception as e:
            print('[memberRatingModel.search]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando os parâmetros      
        if (not is_username(member_rating.student)):
            raise Exception('invalid student parameter.')
        if (not is_classname(member_rating.classname)):
            raise Exception('invalid classname parameter.')
        if (not is_alphanumeric(member_rating.proposal)):
            raise Exception('invalid proposal parameter.')
        if (not is_integer(member_rating.proposal)):   
            raise Exception('invalid lesson number parameter.')

        # 3º Buscando o usuario
        try:
            member_rating = MemberRatingDAO().select(member_rating)
            if member_rating is None:
                raise Exception('couldn\'t  not find member rating.')
        except Exception as e:
            raise e

        return dict(member_rating)