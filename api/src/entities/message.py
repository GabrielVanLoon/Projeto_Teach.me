
class Message:
    def __init__(self, classname = None, chat_code = None, message_number = None, username = None, date = None, content = None):
        self.classname      = classname 
        self.chat_code      = chat_code
        self.message_number = message_number
        self.username       = username 
        self.date           = date 
        self.content        = content
        
    def __iter__(self):
        yield classname,        classname
        yield chat_code,        chat_code
        yield message_number,   message_number
        yield username,         username 
        yield date,             date 
        yield content,          content