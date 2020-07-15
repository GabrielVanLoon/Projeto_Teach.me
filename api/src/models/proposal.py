from django.http import QueryDict
import re 

from src.libs.validations import *
from src.entities.proposal import Proposal
from src.dao.proposal import ProposalDAO

class ProposalModel:

    def register(self, args:QueryDict = None):
        proposal = None

        # 1º Pegando os parâmetros de interesse
        try: 
            proposal = Proposal(None, args.get('classname', '').strip(), args.get('instructor', '').strip(), args.get('subject', '').strip(), 
                1, 'EM APROVAÇÃO', None, 0.00)
        except Exception as e:
            print('[proposalModel.register]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando inputs 
        if (not is_username(proposal.instructor)):
            raise Exception('invalid instructor parameter.')
        if (not is_classname(proposal.classname)):
            raise Exception('invalid classname parameter.')
        if (len(proposal.subject) < 2) or (not is_alphanumeric(proposal.subject, with_spaces=True)):
            raise Exception('invalid subject parameter.')

            # @TODO: Gerar código baseado na qtd de propostas antigas
            # @TODO: Calcular full_price baseado na soma de preço das aulas
            # @TODO: Nível de acesso: o criador é líder?
            # @TODO: Etc...

        # 3º Realizando o registro
        try:
            ProposalDAO().insert(proposal)
        except Exception as e:
            raise e

    def update(self, args:QueryDict = None):        
        # @TODO:    Nem perdi tempo fazendo pq maioria dos updates
        #            que imaginei seriam disparados pelo próprio sistema.
        raise Exception('proposal not found. Please check if the instructor and subject params are valid!')
        

    def search(self, args:QueryDict = None):
        proposal = None

        # 1º Extraindo parâmetros de interesse
        try: 
            proposal = proposal = Proposal(args.get('id', '').strip(), args.get('classname', '').strip(), args.get('instructor', '').strip(), args.get('subject', '').strip(), 
                args.get('code', '').strip())
        except Exception as e:
            print('[proposalModel.search]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando os parâmetros      
        if (not is_username(proposal.instructor)):
            raise Exception('invalid instructor parameter.')
        if (not is_classname(proposal.classname)):
            raise Exception('invalid classname parameter.')
        if (len(proposal.subject) < 2) or (not is_alphanumeric(proposal.subject, with_spaces=True)):
            raise Exception('invalid subject parameter.')
        if (not is_integer(proposal.code)):
            raise Exception('invalid code parameter.')

        # 3º Buscando o usuario
        try:
            proposal = ProposalDAO().select(proposal)
            if proposal is None:
                raise Exception('couldn\'t  not find proposal.')
        except Exception as e:
            raise e

        return dict(proposal)