
class MemberRating:
    def __init__(self, student = None, classname = None, proposal = None, lesson_number = None, rate = None):
        self.student = student
        self.classname = classname 
        self.proposal = proposal 
        self.lesson_number = lesson_number 
        self.rate = rate
    
    def __iter__(self):
        yield 'student',        self.student
        yield 'classname',      self.classname
        yield 'proposal',       self.proposal
        yield 'lesson_number',  self.lesson_number
        yield 'rate',           self.rate