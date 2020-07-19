from django.http    import JsonResponse
from rest_framework import status

from src.models.proposal import ProposalModel

class ProposalController:

    def register(self, request):
        (data, http_status)   = ({ }, status.HTTP_400_BAD_REQUEST)
        
        if request.method != 'POST':
            data = { 'error': 'invalid http method. Use POST instead.'}
            return JsonResponse(data, status=http_status)

        try:
            ProposalModel().register(request.POST)
            data = { 'message': 'successfully registered proposal.'}
            http_status = status.HTTP_200_OK

        except Exception as e:
            data = { 'error': str(e) }

        return JsonResponse(data, status=http_status)

    def update(self, request):
        (data, http_status)   = ({ }, status.HTTP_400_BAD_REQUEST)
        # @TODO: Nem perdi tempo fazendo pq maioria dos updates
        #        que imaginei seriam disparados pelo próprio sistema.
        return JsonResponse(data, status=http_status)


    def search(self, request):
        (data, http_status)   = ({ }, status.HTTP_400_BAD_REQUEST)
        
        if request.method != 'GET':
            data = { 'error': 'invalid http method. Use GET instead.'}
            return JsonResponse(data, status=http_status)

        try:
            proposal = ProposalModel().search(request.GET)
            data = { 'proposal': proposal }
            http_status = status.HTTP_200_OK

        except Exception as e:
            data = { 'error': str(e) }

        return JsonResponse(data, status=http_status)

    def get_proposals(self, request):
        (data, http_status)   = ({ }, status.HTTP_400_BAD_REQUEST)
        
        if request.method != 'POST':
            data = { 'error': 'invalid http method. Use GET instead.'}
            return JsonResponse(data, status=http_status)

        try:
            n_rows, proposals = ProposalModel().get_proposals(request.POST)
            data = { 
                'message': '{} proposal(s) found'.format(n_rows),
                'rows': n_rows,
                'proposals': proposals,
                }
            http_status = status.HTTP_200_OK

        except Exception as e:
            data = { 'error': str(e) }

        return JsonResponse(data, status=http_status)