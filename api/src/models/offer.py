from django.http import QueryDict
import re 

from src.libs.validations import is_username, is_alphanumeric, is_numeric
from src.entities.offer import Offer
from src.dao.offer import OfferDAO

class OfferModel:

    def register(self, args:QueryDict = None):
        offer = None

        # 1º Pegando os parâmetros de interesse
        try: 
            offer = Offer(args.get('instructor', '').strip(), args.get('subject', '').strip(), args.get('base_price', '').strip(), args.get('methodology', '').strip())
        except Exception as e:
            print('[offerModel.register]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando inputs 
        if (not is_username(offer.instructor)):
            raise Exception('invalid instructor parameter.')
        if (len(offer.subject) < 2) or (not is_alphanumeric(offer.subject, with_spaces=True)):
            raise Exception('invalid subject parameter.')
        if (not is_numeric(offer.base_price)): 
            raise Exception('invalid base price parameter.')
        
        offer.base_price = float("{:.2f}".format(offer.base_price))

        # 3º Realizando o registro
        try:
            OfferDAO().insert(offer)
        except Exception as e:
            raise e


    def update(self, args:QueryDict = None):
        # 1º Extraindo parâmetros de interesse
        try:
            offer = Offer(args.get('instructor', '').strip(), args.get('subject', '').strip(), args.get('base_price', '').strip(), args.get('methodology', '').strip())
        except Exception as e:
            print('[offerModel.update]', str(e))
            raise Exception('invalid arguments.')
        
        # 2º Validando inputs        
        if (not is_username(offer.instructor)):
            raise Exception('invalid instructor parameter.')
        if (len(offer.subject) < 2) or (not is_alphanumeric(offer.subject, with_spaces=True)):
            raise Exception('invalid subject parameter.')
        if (not is_numeric(offer.base_price)): 
            raise Exception('invalid base price parameter.')
        
        offer.base_price = float("{:.2f}".format(offer.base_price))

        # 3º Atualizando a tabela
        try:
            rows_affected = OfferDAO().update(offer)
            if rows_affected != 1:
                raise Exception('offer not found. Please check if the instructor and subject params are valid!')
        except Exception as e:
            raise e

    def search(self, args:QueryDict = None):
        offer = None

        # 1º Extraindo parâmetros de interesse
        try: 
            offer = Offer(args.get('instructor', '').strip(), args.get('subject', '').strip())
        except Exception as e:
            print('[offerModel.search]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando os parâmetros      
        if (not is_username(offer.instructor)):
            raise Exception('invalid instructor parameter.')
        if (len(offer.subject) < 2) or (not is_alphanumeric(offer.subject, with_spaces=True)):
            raise Exception('invalid subject parameter.')

        # 3º Buscando o usuario
        try:
            offer = OfferDAO().select(offer)
            if offer is None:
                raise Exception('couldn\'t  not find offer.')
        except Exception as e:
            raise e

        return dict(offer)