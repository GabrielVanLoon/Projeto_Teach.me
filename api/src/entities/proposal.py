#Used classname instead of class
class Proposal:
    def __init__(self, id=None, classname=None, instructor=None, subject=None, code=None, status=None, creation_date=None, full_price=None):
        self.id = id
        self.classname = classname
        self.instructor = instructor
        self.subject = subject
        self.code = code
        self.status = status
        self.creation_date = creation_date
        self.full_price = full_price