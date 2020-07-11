from django.http import JsonResponse

from src.models.usuario import *


class UsuarioController: 

    def cadastrar(self, request):
        try:
            print(request.POST)
            UsuarioModel().cadastrar(request.POST.get('nome', ''), 'Blabla')
            data = {
                'message': 'Usuário cadastrado com sucesso',
            }
            return JsonResponse(data)
        except Exception as err:
            data = {
                'error': str(err)
            }
            return JsonResponse(data, status=500)



    
