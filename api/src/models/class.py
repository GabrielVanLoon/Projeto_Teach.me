from src.dao.class import Class
from src.dao.class import ClassDAO

class ClassModel:

    def register(self, args=None):
        class_ = None
        
        # 1 - Pegando os parâmetros de interesse
        try:
            class_ = Class(args.get('classname').strip(), args.get('title').strip(), args.get('description').strip(),
            None, 1, args.get('max_members').strip(), args.get('situation').strip())
        except:
            raise('invalid arguments.')
        
        # 2 - Validando inputs
        # @TODO: Checar se classname ja existe ou se existe um username igual a classname
        if (class_.classname == '') or (len(class_.classname) < 2):
            raise('invalid classname')
        if class_.title == '':
            raise('invalid title')
        if (class_.max_members < 0) or (class_.max_members > 50):
            raise('invalid max number of members')

        try:
            ClassDAO().insert(class_)
        except Exception as e:
            raise e

        return None
    
    def update(self, args = {}):
        return None

    def search(self, args = {}):
        return None