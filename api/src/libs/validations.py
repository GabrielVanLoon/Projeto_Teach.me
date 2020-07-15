import re 

def is_valid_mail(param:str = ''):
    return re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', param)

def is_integer(param:str = ''):
    return re.search('^[0-9]{1,}$', param)

def is_numeric(param:str = ''):
    return re.search('^[0-9.]{1,}$', param)

def is_alphabetic(param:str = '', with_spaces:bool = False):
    if with_spaces:
        return re.search('^[a-zA-Z\s]{1,}$', param)
    else:
        return re.search('^[a-zA-Z]{1,}$', param) 

def is_alphanumeric(param:str = '', with_spaces:bool = False):
    if with_spaces:
        return re.search('^[a-zA-Z0-9\s]{1,}$', param)
    else:
        return re.search('^[a-zA-Z0-9]{1,}$', param) 

def is_username(param:str = ''):
    return re.search('^[a-zA-Z0-9-_]{1,}$', param)

def is_classname(param:str = ''):
    return re.search('^[a-zA-Z0-9-_]{1,}$', param)
    
