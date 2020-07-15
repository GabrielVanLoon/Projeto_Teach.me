from django.http import QueryDict
import re 

from src.libs.validations import is_username, is_alphanumeric, is_numeric
from src.entities.recommendation import Recommendation
from src.dao.recommendation import RecommendationDAO

class RecommendationModel:

    def register(self, args:QueryDict = None):
        recommendation = None

        # 1º Pegando os parâmetros de interesse
        try: 
            recommendation = Recommendation(args.get('student', '').strip(), args.get('instructor', '').strip(), args.get('text', '').strip())
        except Exception as e:
            print('[recommendationModel.register]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando inputs 
        if (not is_username(recommendation.student)):
            raise Exception('invalid student parameter.')
        if (not is_username(recommendation.instructor)):
            raise Exception('invalid instructor parameter.')
        if (len(recommendation.text) < 3):
             raise Exception('invalid text parameter. Must be at least 3 characters long.')

        # 3º Realizando o registro
        try:
            RecommendationDAO().insert(recommendation)
        except Exception as e:
            raise e


    def update(self, args:QueryDict = None):
        # 1º Extraindo parâmetros de interesse
        try:
            recommendation = Recommendation(args.get('student', '').strip(), args.get('instructor', '').strip(), args.get('text', '').strip())
        except Exception as e:
            print('[recommendationModel.update]', str(e))
            raise Exception('invalid arguments.')
              
        # 2º Validando inputs 
        if (not is_username(recommendation.student)):
            raise Exception('invalid student parameter.')
        if (not is_username(recommendation.instructor)):
            raise Exception('invalid instructor parameter.')
        if (len(recommendation.text) < 3):
             raise Exception('invalid text parameter. Must be at least 3 characters long.')

        # 3º Atualizando a tabela
        try:
            rows_affected = RecommendationDAO().update(recommendation)
            if rows_affected != 1:
                raise Exception('recommendation not found. Please check if the student and instructor parameters are valid!')
        except Exception as e:
            raise e

    def search(self, args:QueryDict = None):
        recommendation = None

        # 1º Extraindo parâmetros de interesse
        try: 
            recommendation = Recommendation(args.get('student', '').strip(), args.get('instructor', '').strip(), args.get('text', '').strip())
        except Exception as e:
            print('[recommendationModel.search]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando inputs 
        if (not is_username(recommendation.student)):
            raise Exception('invalid student parameter.')
        if (not is_username(recommendation.instructor)):
            raise Exception('invalid instructor parameter.')

        # 3º Buscando o usuario
        try:
            recommendation = RecommendationDAO().select(recommendation)
            if recommendation is None:
                raise Exception('couldn\'t  not find recommendation.')
        except Exception as e:
            raise e

        return dict(recommendation)