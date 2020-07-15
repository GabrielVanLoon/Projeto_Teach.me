
class AvailableTime:
    def __init__(self, instructor = None, weekday = None, time = None ):
        self.instructor = instructor 
        self.weekday = weekday 
        self.time = time

    def __iter__(self):
        yield 'instructor',   self.instructor
        yield 'weekday',      self.weekday
        yield 'time',         self.time