from django.http import QueryDict
import re 

from src.libs.validations import is_username, is_alphanumeric, is_numeric
from src.entities.available_time import AvailableTime
from src.dao.available_time import AvailableTimeDAO

class AvailableTimeModel:

    def register(self, args:QueryDict = None):
        available_time = None

        # 1º Pegando os parâmetros de interesse
        try: 
            available_time = AvailableTime(args.get('instructor', '').strip(), args.get('weekday', '').strip(), args.get('time', '').strip())
        except Exception as e:
            print('[availableTimeModel.register]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando inputs 
        if (not is_username(available_time.instructor)):
            raise Exception('invalid instructor parameter.')
        if (available_time.weekday not in ['DOM', 'SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SAB']):
            raise Exception('invalid weekday parameter.')
        
        # @TODO: Lidar com a validação e conversão de available_time.time para TIME (postgresql)
        
        # 3º Realizando o registro
        try:
            AvailableTimeDAO().insert(available_time)
        except Exception as e:
            raise e


    def search(self, args:QueryDict = None):
        available_time = None

        # 1º Extraindo parâmetros de interesse
        try: 
            available_time = AvailableTime(args.get('instructor', '').strip(), args.get('weekday', '').strip(), args.get('time', '').strip())
        except Exception as e:
            print('[availableTimeModel.search]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando os parâmetros      
        if (not is_username(available_time.instructor)):
            raise Exception('invalid instructor parameter.')
        if (available_time.weekday not in ['DOM', 'SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SAB']):
            raise Exception('invalid weekday parameter.')
        
        # @TODO: Lidar com a validação e conversão de available_time.time para TIME (postgresql)

        # 3º Buscando o usuario
        try:
            available_time = AvailableTimeDAO().select(available_time)
            if available_time is None:
                raise Exception('couldn\'t  not find available_time.')
        except Exception as e:
            raise e

        return dict(available_time)