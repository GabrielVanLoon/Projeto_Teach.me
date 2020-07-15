from django.http import QueryDict
import re 

from src.libs.validations import is_username, is_alphanumeric, is_numeric
from src.entities.accepts import Accepts
from src.dao.accepts import AcceptsDAO

class AcceptsModel:

    def register(self, args:QueryDict = None):
        accepts = None

        # 1º Pegando os parâmetros de interesse
        try: 
            accepts = Accepts(args.get('student', '').strip(), args.get('classname', '').strip(), args.get('proposal', '').strip())
        except Exception as e:
            print('[acceptsModel.register]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando inputs 
        if (not is_username(accepts.student)):
            raise Exception('invalid student parameter.')
        if (not is_classname(accepts.classname)):
            raise Exception('invalid classname parameter.')
        if (not is_integer(accepts.proposal)):
            raise Exception('invalid proposal parameter.')

        # 3º Realizando o registro
        try:
            AcceptsDAO().insert(accepts)
        except Exception as e:
            raise e

    def search(self, args:QueryDict = None):
        accepts = None

        # 1º Extraindo parâmetros de interesse
        try: 
            accepts = Accepts(args.get('student', '').strip(), args.get('classname', '').strip(), args.get('proposal', '').strip())
        except Exception as e:
            print('[acceptsModel.search]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando inputs 
        if (not is_username(accepts.student)):
            raise Exception('invalid student parameter.')
        if (not is_classname(accepts.classname)):
            raise Exception('invalid classname parameter.')
        if (not is_integer(accepts.proposal)):
            raise Exception('invalid proposal parameter.')

        # 3º Buscando o usuario
        try:
            accepts = AcceptsDAO().select(accepts)
            if accepts is None:
                raise Exception('could not find accepts.')
        except Exception as e:
            raise e

        return dict(accepts)