from django.http import JsonResponse
from rest_framework import status

from src.models.class_ import *

class ClassController: 

    def register(self, request):
        (data, http_status)   = ({ }, status.HTTP_400_BAD_REQUEST)
  
        if request.method != 'POST':
            data = { 'error': 'invalid http method.'}
            return JsonResponse(data, status=http_status)

        try:
            ClassModel().register(request.POST)
            data = { 'message': 'successfully registered class.'}
            http_status = status.HTTP_200_OK

        except Exception as e:  
            data = { 'error': str(e) }

        return JsonResponse(data, status=http_status)

    def update(self, request):
        return None

    def search(self, request):
        return None