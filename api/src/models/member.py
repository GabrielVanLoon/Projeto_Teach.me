from django.http import QueryDict
import re 

from src.libs.validations import is_username, is_classname
from src.entities.member import Member
from src.dao.member import MemberDAO

class MemberModel:

    def register(self, args:QueryDict = None):
        member = None

        # 1º Pegando os parâmetros de interesse
        try: 
            member = Member(args.get('student', '').strip(), args.get('study_class', '').strip(), args.get('is_leader', '0').strip())
        except Exception as e:
            print('[memberModel.register]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando inputs        
        if (member.student == '') or (len(member.student) < 2) or (not is_username(member.student)):
            raise Exception('invalid student parameter.')
        if (member.study_class == '') or (len(member.study_class) < 2) or (not is_classname(member.study_class)):
            raise Exception('invalid study class parameter.')
        if member.is_leader not in ['0', '1']:
            raise Exception('invalid is leader parameter.')
        
        member.is_leader = True if member.is_leader == '1' else False

        # 3º Realizando o registro
        try:
            MemberDAO().insert(member)
        except Exception as e:
            raise e


    def update(self, args:QueryDict = None):
        # 1º Extraindo parâmetros de interesse
        try:
            member = Member(args.get('student', '').strip(), args.get('study_class', '').strip(), args.get('is_leader', '0').strip())
        except Exception as e:
            print('[memberModel.update]', str(e))
            raise Exception('invalid arguments.')
        
        # 2º Validando inputs        
        if (member.student == '') or (len(member.student) < 2) or (not is_username(member.student)):
            raise Exception('invalid student parameter.')
        if (member.study_class == '') or (len(member.study_class) < 2) or (not is_classname(member.study_class)):
            raise Exception('invalid study class parameter.')
        if member.is_leader not in ['0', '1']:
            raise Exception('invalid is leader parameter.')
        
        member.is_leader = True if member.is_leader == '1' else False

        # 3º Atualizando a tabela
        try:
            rows_affected = MemberDAO().update(member)
            if rows_affected != 1:
                raise Exception('member not found. Please check if the student and study_class params are valid!')
        except Exception as e:
            raise e

    def search(self, args:QueryDict = None):
        member = None

        # 1º Extraindo parâmetros de interesse
        try: 
            member = Member(args.get('student', '').strip(), args.get('study_class', '').strip())
        except Exception as e:
            print('[memberModel.search]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando os parâmetros      
        if (member.student == '') or (len(member.student) < 2) or (not is_username(member.student)):
            raise Exception('invalid student parameter.')
        if (member.study_class == '') or (len(member.study_class) < 2) or (not is_classname(member.study_class)):
            raise Exception('invalid study class parameter.')

        # 3º Buscando o usuario
        try:
            member = MemberDAO().select(member)
            if member is None:
                raise Exception('couldn\'t  not find member.')
        except Exception as e:
            raise e

        return dict(member)