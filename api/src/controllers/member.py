from django.http    import JsonResponse
from rest_framework import status

from src.models.member import MemberModel

class MemberController:

    def register(self, request):
        (data, http_status)   = ({ }, status.HTTP_400_BAD_REQUEST)
        
        if request.method != 'POST':
            data = { 'error': 'invalid http method. Use POST instead.'}
            return JsonResponse(data, status=http_status)

        try:
            MemberModel().register(request.POST)
            data = { 'message': 'successfully registered member.'}
            http_status = status.HTTP_200_OK

        except Exception as e:
            data = { 'error': str(e) }

        return JsonResponse(data, status=http_status)

    def update(self, request):
        (data, http_status)   = ({ }, status.HTTP_400_BAD_REQUEST)
        
        if request.method != 'POST':
            data = { 'error': 'invalid http method. Use POST instead.'}
            return JsonResponse(data, status=http_status)

        try:
            MemberModel().update(request.POST)
            data = { 'message': 'successfully updated member.'}
            http_status = status.HTTP_200_OK

        except Exception as e:
            data = { 'error': str(e) }

        return JsonResponse(data, status=http_status)


    def search(self, request):
        (data, http_status)   = ({ }, status.HTTP_400_BAD_REQUEST)
        
        if request.method != 'GET':
            data = { 'error': 'invalid http method. Use GET instead.'}
            return JsonResponse(data, status=http_status)

        try:
            member = MemberModel().search(request.GET)
            data = { 'member': member }
            http_status = status.HTTP_200_OK

        except Exception as e:
            data = { 'error': str(e) }

        return JsonResponse(data, status=http_status)