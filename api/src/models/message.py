from django.http import QueryDict
import re 

from src.libs.validations import is_username, is_alphanumeric, is_numeric
from src.entities.message import Message
from src.dao.message import MessageDAO

class MessageModel:

    def register(self, args:QueryDict = None):
        message = None

        # 1º Pegando os parâmetros de interesse
        try: 
            message = Message(args.get('classname', '').strip(), args.get('chat_code', '').strip(), args.get('message_number', '').strip(), args.get('username', '').strip(), 
            args.get('date', '').strip(), args.get('content', '').strip())
        except Exception as e:
            print('[messageModel.register]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando inputs
        if (not is_classname(message.classname)):
            raise Exception('invalid classname parameter.')
        if (not is_integer(message.chat_code)):
            raise Exception('invalid chat code parameter.')
        if (not is_integer(message.message_number)):
            raise Exception('invalid message number parameter.')
        if (not is_username(message.username)):
            raise Exception('invalid username parameter.')

        # 3º Realizando o registro
        try:
            MessageDAO().insert(message)
        except Exception as e:
            raise e


    def update(self, args:QueryDict = None):
        # 1º Extraindo parâmetros de interesse
        try: 
            message = Message(args.get('content', '').strip())
        except Exception as e:
            print('[messageModel.register]', str(e))
            raise Exception('invalid arguments.')
              
        # 2º Validando inputs 
        if (not is_classname(message.classname)):
            raise Exception('invalid classname parameter.')
        if (not is_integer(message.chat_code)):
            raise Exception('invalid chat code parameter.')
        if (not is_integer(message.message_number)):
            raise Exception('invalid message number parameter.')
        if (not is_username(message.username)):
            raise Exception('invalid username parameter.')

        # 3º Atualizando a tabela
        try:
            rows_affected = MessageDAO().update(message)
            if rows_affected != 1:
                raise Exception('message not found. Please check if the class_name, chat_code and message_number parameters are valid!')
        except Exception as e:
            raise e

    def search(self, args:QueryDict = None):
        message = None

        # 1º Extraindo parâmetros de interesse
        Message(args.get('classname', '').strip(), args.get('username', '').strip(), args.get('date', '').strip(), args.get('content', '').strip())
        except Exception as e:
            print('[messageModel.register]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando inputs 
        if (not is_classname(message.classname)):
            raise Exception('invalid classname parameter.')
        if (not is_integer(message.chat_code)):
            raise Exception('invalid chat code parameter.')
        if (not is_integer(message.message_number)):
            raise Exception('invalid message number parameter.')

        # 3º Buscando o usuario
        try:
            message = MessageDAO().select(message)
            if message is None:
                raise Exception('could not find message.')
        except Exception as e:
            raise e

        return dict(message)