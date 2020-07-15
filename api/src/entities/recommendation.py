class Recommendation:
    def __init__(self, student=None, instructor=None, text=None):
        self.student = student
        self.instructor = instructor
        self.text = text

    def __iter__(self):
        yield 'student',   self.student
        yield 'instructor',      self.instructor
        yield 'text',   self.text