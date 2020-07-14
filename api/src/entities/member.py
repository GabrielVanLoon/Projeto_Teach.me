class Member:
    def __init__(self, student=None, study_class=None, is_leader=None):
        self.student = student
        self.study_class = study_class
        self.is_leader = is_leader

    def __iter__(self):
        yield 'student',        self.student
        yield 'study_class',    self.study_class
        yield 'is_leader',       self.is_leader
