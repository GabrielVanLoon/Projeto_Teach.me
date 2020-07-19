
class Lesson:
    def __init__(self, proposal = None, lesson_number = None, instructor = None, place = None, full_price = None, status = None, start = None, end = None, instructor_rate = None):
        self.proposal = proposal 
        self.lesson_number = lesson_number 
        self.instructor = instructor 
        self.place = place 
        self.full_price = full_price 
        self.status = status 
        self.start = start 
        self.end = end 
        self.instructor_rate = instructor_rate

    def __iter__(self):
        yield 'proposal',         self.proposal 
        yield 'lesson_number',    self.lesson_number 
        yield 'instructor',       self.instructor 
        yield 'place',            self.place 
        yield 'full_price',       self.full_price 
        yield 'status',           self.status 
        yield 'start',            self.start 
        yield 'end',              self.end 
        yield 'instructor_rate',  self.instructor_rate