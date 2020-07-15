from django.http import QueryDict
import re 

from src.libs.validations import is_username, is_alphanumeric, is_numeric
from src.entities.lesson import Lesson
from src.dao.lesson import LessonDAO

class LessonModel:

    def register(self, args:QueryDict = None):
        lesson = None

        # 1º Pegando os parâmetros de interesse
        try: 
            lesson = Lesson(args.get('proposal', '').strip(), args.get('lesson_number', '').strip(), args.get('instructor', '').strip(), args.get('place', '').strip(), args.get('full_price', '').strip(), 
            args.get('status', '').strip(), args.get('start', '').strip(), args.get('end', '').strip(), args.get('instructor_rate', '').strip())
        except Exception as e:
            print('[lessonModel.register]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando inputs
        if (not is_integer(lesson.proposal)):
            raise Exception('invalid proposal parameter.')
        if (not is_integer(lesson.lesson_number)):
            raise Exception('invalid lesson number parameter.')
        if (not is_username(lesson.instructor)) or (lesson.instructor < 2):
            raise Exception('invalid instructor parameter.')
        if (not is_alphanumeric(lesson.place)):
            raise Exception('invalid place parameter.')
        if (not is_numeric(lesson.full_price)) or (float(lesson.full_price) < 0):
            raise Exception('invalid full price parameter.')
            

        # 3º Realizando o registro
        try:
            LessonDAO().insert(lesson)
        except Exception as e:
            raise e


    def update(self, args:QueryDict = None):
        # 1º Extraindo parâmetros de interesse
        try: 
            lesson = Lesson(args.get('full_price', '').strip(), args.get('status', '').strip(), args.get('start', '').strip(), args.get('end', '').strip(), args.get('instructor_rate', '').strip())
        except Exception as e:
            print('[lessonModel.register]', str(e))
            raise Exception('invalid arguments.')
              
        # 2º Validando inputs 
        if (not is_integer(lesson.proposal)):
            raise Exception('invalid proposal parameter.')
        if (not is_integer(lesson.lesson_number)):
            raise Exception('invalid lesson number parameter.')
        if (not is_username(lesson.instructor)) or (lesson.instructor < 2):
            raise Exception('invalid instructor parameter.')
        if (not is_alphanumeric(lesson.place)):
            raise Exception('invalid place parameter.')
        if (not is_numeric(lesson.full_price)) or (float(lesson.full_price) < 0):
            raise Exception('invalid full price parameter.')

        # 3º Atualizando a tabela
        try:
            rows_affected = LessonDAO().update(lesson)
            if rows_affected != 1:
                raise Exception('lesson not found. Please check if the proposal and lesson_number parameters are valid!')
        except Exception as e:
            raise e

    def search(self, args:QueryDict = None):
        lesson = None

        # 1º Extraindo parâmetros de interesse
        Lesson(args.get('proposal', '').strip(), args.get('lesson_number', '').strip())
        except Exception as e:
            print('[lessonModel.register]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando inputs 
        if (not is_integer(lesson.proposal)):
            raise Exception('invalid proposal parameter.')
        if (not is_integer(lesson.lesson_number)):
            raise Exception('invalid lesson number parameter.')

        # 3º Buscando o usuario
        try:
            lesson = LessonDAO().select(lesson)
            if lesson is None:
                raise Exception('could not find lesson.')
        except Exception as e:
            raise e

        return dict(lesson)