from django.http import QueryDict
import re 

from src.libs.validations import is_username, is_classname, is_integer
from src.entities.chat import Chat
from src.dao.chat import ChatDAO

class ChatModel:

    def register(self, args:QueryDict = None):
        chat = None

        # 1º Pegando os parâmetros de interesse
        try: 
            chat = Chat(args.get('classname', '').strip(), None, None, '', args.get('instructor', '').strip())
        except Exception as e:
            print('[chatModel.register]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando inputs 
        if (not is_classname(chat.classname)):
            raise Exception('invalid classname parameter.')
        if (chat.instructor != '') and (not is_username(chat.instructor)):
            raise Exception('invalid instructor parameter.')
        
        # @TODO: Gerar nome do chat baseado na sua intenção
        # @TODO: Enumerar os possiveis status do chat
        # @TODO: Gerar valor do código baseado na quantidade de outros chats da turma

        # 3º Realizando o registro
        try:
            ChatDAO().insert(chat)
        except Exception as e:
            raise e


    def update(self, args:QueryDict = None):
        # 1º Extraindo parâmetros de interesse
        try:
            chat = Chat(args.get('classname', '').strip(), args.get('chat_code', '').strip(), args.get('name', '').strip(), 
                            args.get('status', '').strip(), args.get('instructor', '').strip())
        except Exception as e:
            print('[chatModel.update]', str(e))
            raise Exception('invalid arguments.')
        
        # 2º Validando inputs        
        if (not is_classname(chat.classname)):
            raise Exception('invalid classname parameter.')
        if (not is_integer(chat.chat_code)):
            raise Exception('invalid chat code parameter.')
        
        # @TODO: Gerar nome do chat baseado na sua intenção
        # @TODO: Enumerar os possiveis status do chat

        # 3º Atualizando a tabela
        try:
            rows_affected = ChatDAO().update(chat)
            if rows_affected != 1:
                raise Exception('chat not found. Please check if the parameters are valid!')
        except Exception as e:
            raise e

    def search(self, args:QueryDict = None):
        chat = None

        # 1º Extraindo parâmetros de interesse
        try: 
            chat = Chat(args.get('classname', '').strip(), args.get('chat_code', '').strip())
        except Exception as e:
            print('[chatModel.search]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando os parâmetros         
        if (not is_classname(chat.classname)):
            raise Exception('invalid classname parameter.')
        if (not is_integer(chat.chat_code)):
            raise Exception('invalid chat code parameter.')

        # 3º Buscando o usuario
        try:
            chat = ChatDAO().select(chat)
            if chat is None:
                raise Exception('couldn\'t  not find chat.')
        except Exception as e:
            raise e

        return dict(chat)