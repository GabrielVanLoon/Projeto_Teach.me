
class Chat:
    def __init__(self, classname = None, chat_code = None, name = None, status = None, instructor = None):
        self.classname = classname 
        self.chat_code = chat_code
        self.name = name 
        self.status = status 
        self.instructor = instructor
    
    def __iter__(self):
        yield 'classname',   self.classname
        yield 'chat_code',      self.chat_code
        yield 'name',   self.name
        yield 'status',       self.status
        yield 'instructor',  self.instructor
        
