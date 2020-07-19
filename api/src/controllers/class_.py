from django.http import JsonResponse
from rest_framework import status

from src.models.class_ import ClassModel

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
        (data, http_status)   = ({ }, status.HTTP_400_BAD_REQUEST)
        
        if request.method != 'POST':
            data = { 'error': 'invalid http method. Use POST instead.'}
            return JsonResponse(data, status=http_status)

        try:
            ClassModel().update(request.POST)
            data = { 'message': 'successfully updated class.'}
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
            class_ = ClassModel().search(request.GET)
            data = { 'class': class_ }
            http_status = status.HTTP_200_OK

        except Exception as e:
            data = { 'error': str(e) }

        return JsonResponse(data, status=http_status)

    def get_classes(self, request):
        (data, http_status)   = ({ }, status.HTTP_400_BAD_REQUEST)
        
        if request.method != 'POST':
            data = { 'error': 'invalid http method. Use POST instead.'}
            return JsonResponse(data, status=http_status)
        try:
            n_rows, classes_dict = ClassModel().get_classes(request.POST)
            data = {
                'message': '% classes found'.format(n_rows),
                'rows': n_rows,
                'results': classes_dict,
            }
            http_status = status.HTTP_200_OK
        except Exception as e:
            data = { 'error': str(e) }
        return JsonResponse(data, status=http_status)