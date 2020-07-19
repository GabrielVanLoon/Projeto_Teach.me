from django.http import QueryDict
import re 

from src.libs.validations import *
from src.entities.proposal import Proposal
from src.entities.lesson import Lesson
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

    def get_proposals(self, args:QueryDict = None):
        proposals = [ ]
        return_proposals = [ ]
        n_rows = 0

        username = ''
        status   = ''
        # 1º Extraindo parâmetros de interesse
        try: 
            username = args.get('username', '').strip()
            status = args.get('status', '').strip()
        except Exception as e:
            print('[proposalModel.get_proposals]', str(e))
            raise Exception('invalid arguments.')

        # 2º Validando os parâmetros      
        if (not is_username(username)):
            raise Exception('invalid username parameter.')

        # 3º Buscando o usuario
        try:
            n_rows, proposals = ProposalDAO().select_by_student(username, status)
            if proposals is None:
                raise Exception('couldn\'t  not find proposal.')
        except Exception as e:
            raise e
        
        print(proposals)

        # 4º Formatando as respostas
        for p in proposals:
            temp_proposal = Proposal(id=p[0],classname=p[1],instructor=p[2],subject=p[3],code=p[4],status=p[5],creation_date=p[6],full_price=p[7])
            temp_proposal = dict(temp_proposal)

            temp_lesson  = Lesson(lesson_number=p[8],place=p[9],status=p[10],full_price=p[11],start=p[12])
            temp_lesson = dict(temp_lesson)
            temp_accept =  p[13] 

            # Verificando se já cadastrou a proposta
            proposta_repetida = False
            
            for i in return_proposals:
                if (i['id'] == temp_proposal['id']):
                    i['lessons'].append(temp_lesson)
                    proposta_repetida = True
                    break

            if proposta_repetida == False:
                temp_proposal['accept'] = temp_accept
                temp_proposal['lessons'] = []
                temp_proposal['lessons'].append(temp_lesson)

                return_proposals.append(temp_proposal)
        
        return (n_rows, return_proposals)