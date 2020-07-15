#classname used instead of class
class Accepts:
    def __init__(self, student=None, classname=None, proposal=None):
        self.student = student
        self.classname = classname
        self.proposal = proposal

    def __iter__(self):
        yield 'student',    student
        yield 'classname',  classname
        yield 'proposal',   proposal