from django.http    import JsonResponse
from rest_framework import status

from src.models.user   import UserModel

class UserController:

    def register(self, request):
        (data, http_status)   = ({ }, status.HTTP_400_BAD_REQUEST)
        
        if request.method != 'POST':
            data = { 'error': 'invalid http method. Use POST instead.'}
            return JsonResponse(data, status=http_status)

        try:
            UserModel().register(request.POST)
            data = { 'message': 'successfully registered user.'}
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
            UserModel().update(request.POST)
            data = { 'message': 'successfully updated user.'}
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
            user = UserModel().search(request.GET)
            data = { 'user': user }
            http_status = status.HTTP_200_OK

        except Exception as e:
            data = { 'error': str(e) }

        return JsonResponse(data, status=http_status)

    def login(self, request):
        (data, http_status)   = ({ }, status.HTTP_400_BAD_REQUEST)
        
        if request.method != 'POST':
            data = { 'error': 'invalid http method. Use POST instead.'}
            return JsonResponse(data, status=http_status)
        try:
            user = UserModel().login(request.POST)
            if(user is not None):
                data = { 
                    'message': 'successfully logged in.',
                    'username': user.username,
                    'name' : user.name,
                    'last_name' : user.last_name,
                    'email' : user.email,
                    'is_instructor' : user.is_instructor
                }
            http_status = status.HTTP_200_OK
        except Exception as e:
            data = { 'error': str(e) }
        return JsonResponse(data, status=http_status)

    def check_username(self, request):
        (data, http_status)   = ({ }, status.HTTP_400_BAD_REQUEST)
        
        if request.method != 'POST':
            data = { 'error': 'invalid http method. Use POST instead.'}
            return JsonResponse(data, status=http_status)
        try:
            UserModel().check_username(request.POST)
            data = { 'message': 'username is available.' }
            http_status = status.HTTP_200_OK
        except Exception as e:
            data = { 'error': str(e) }
        return JsonResponse(data, status=http_status)
