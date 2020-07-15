
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
        yield proposal,         proposal 
        yield lesson_number,    lesson_number 
        yield instructor,       instructor 
        yield place,            place 
        yield full_price,       full_price 
        yield status,           status 
        yield start,            start 
        yield end,              end 
        yield instructor_rate,  instructor_rate