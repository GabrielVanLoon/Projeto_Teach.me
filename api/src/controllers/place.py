from django.http import JsonResponse
from rest_framework import status

from src.models.place import PlaceModel

class PlaceController: 

    def register(self, request):
        (data, http_status)   = ({ }, status.HTTP_400_BAD_REQUEST)
  
        if request.method != 'POST':
            data = { 'error': 'invalid http method.'}
            return JsonResponse(data, status=http_status)

        try:
            SubjectModel().register(request.POST)
            data = { 'message': 'successfully registered place.'}
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
            PlaceModel().update(request.POST)
            data = { 'message': 'successfully updated place.'}
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
            place = PlaceModel().search(request.GET)
            data = { 'place': place }
            http_status = status.HTTP_200_OK

        except Exception as e:
            data = { 'error': str(e) }

        return JsonResponse(data, status=http_status)