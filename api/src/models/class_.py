from src.dao.class_ import Class
from src.dao.class_ import ClassDAO
from src.libs.validations import *

class ClassModel:

    def register(self, args=None):
        class_ = None
        
        # 1 - Pegando os parâmetros de interesse
        try:
            class_ = Class(args.get('classname').strip(), args.get('title').strip(), args.get('description').strip(),
            None, 1, args.get('max_members').strip(), args.get('situation').strip())
        except:
            raise Exception('invalid arguments.')
        
        # 2 - Validando inputs
        # @TODO: Checar se classname ja existe ou se existe um username igual a classname
        if (class_.classname == '') or (len(class_.classname) < 2) or (not is_classname(class_.classname)):
            raise Exception('invalid classname parameter')
        if class_.title == '':
            raise Exception('invalid title parameter')
        if (not is_integer(class_.max_members)) or (int(class_.max_members) < 0) or (int(class_.max_members) > 50):
            raise Exception('invalid max number of members parameter')

        try:
            ClassDAO().insert(class_)
        except Exception as e:
            raise e

        return None
    
    def update(self, args = {}):
        return None

    def search(self, args = {}):
        return None
