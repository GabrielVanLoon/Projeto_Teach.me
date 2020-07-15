from django.http import QueryDict
import re 

from src.libs.validations import is_username, is_alphanumeric, is_numeric
from src.entities.place import Place
from src.dao.place import PlaceDAO

class PlaceModel:

    def register(self, args:QueryDict = None):
        place = None

        # 1º Pegando os parâmetros de interesse
        try: 
            place = Place(args.get('instructor', '').strip(), args.get('placename', '').strip(), args.get('capacity', '').strip(), args.get('street', '').strip(), args.get('number', '').strip(), 
            args.get('neighborhood', '').strip(), args.get('complement', '').strip(), args.get('city', '').strip(), args.get('federal_state', '').strip())
        except Exception as e:
            print('[placeModel.register]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando inputs
        if (not is_username(place.instructor)):
            raise Exception('invalid instructor parameter.')
        if (not is_alphanumeric(place.placename)):
            raise Exception('invalid placename parameter.')
        if (not is_integer(place.capacity)) or (int(place.capacity) <= 0):
            raise Exception('invalid capacity parameter.')
        if (not is_alphabetic(place.street) or not is_integer(place.number)) or (int(place.number) <= 0) or not is_alphabetic(place.neighborhood):
            raise Exception('invalid address parameters.')
        if len(place.complement) < 2:
            raise Exception('invalid complement parameter')
        if (not is_alphabetic(place.city)) or (len(place.city) < 2):
            raise Exception('invalid city parameter')
        if (len(place.federal_state) != 2):
            raise Exception('invalid federal state parameter')
        # @TODO: checar se UF existe

        # 3º Realizando o registro
        try:
            PlaceDAO().insert(place)
        except Exception as e:
            raise e


    def update(self, args:QueryDict = None):
        # 1º Extraindo parâmetros de interesse
        try: 
            place = Place(args.get('instructor', '').strip(), args.get('placename', '').strip(), args.get('capacity', '').strip(), args.get('street', '').strip(), args.get('number', '').strip(), 
            args.get('neighborhood', '').strip(), args.get('complement', '').strip(), args.get('city', '').strip(), args.get('federal_state', '').strip())
        except Exception as e:
            print('[placeModel.register]', str(e))
            raise Exception('invalid arguments.')
              
        # 2º Validando inputs 
        if (not is_username(place.instructor)):
            raise Exception('invalid instructor parameter.')
        if (not is_alphanumeric(place.placename)):
            raise Exception('invalid placename parameter.')
        if (not is_integer(place.capacity)) or (int(place.capacity) <= 0):
            raise Exception('invalid capacity parameter.')
        if (not is_alphabetic(place.street) or not is_integer(place.number)) or (int(place.number) <= 0) or not is_alphabetic(place.neighborhood):
            raise Exception('invalid address parameters.')
        if len(place.complement) < 2:
            raise Exception('invalid complement parameter')
        if (not is_alphabetic(place.city)) or (len(place.city) < 2):
            raise Exception('invalid city parameter')
        if (len(place.federal_state) != 2):
            raise Exception('invalid federal state parameter')
        # @TODO: checar se UF existe

        # 3º Atualizando a tabela
        try:
            rows_affected = PlaceDAO().update(place)
            if rows_affected != 1:
                raise Exception('place not found. Please check if the instructor and placename parameters are valid!')
        except Exception as e:
            raise e

    def search(self, args:QueryDict = None):
        place = None

        # 1º Extraindo parâmetros de interesse
        Place(args.get('instructor', '').strip(), args.get('placename', '').strip())
        except Exception as e:
            print('[placeModel.register]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando inputs 
        if (not is_username(place.instructor)):
            raise Exception('invalid instructor parameter.')
        if (not is_alphanumeric(place.placename)):
            raise Exception('invalid placename parameter.')

        # 3º Buscando o usuario
        try:
            place = PlaceDAO().select(place)
            if recommendation is None:
                raise Exception('could not find place.')
        except Exception as e:
            raise e

        return dict(recommendation)