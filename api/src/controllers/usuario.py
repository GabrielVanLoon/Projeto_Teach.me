from django.http import JsonResponse
from src.models.usuario import UsuarioModel

# Controller: Lida com a requisição
# - Tipos de validação: verificar método da requisição
# - Conversa com os Models
# - Retorno: JSON + Código de Retorno (200 - SUCCESS, 400 - Erro na requisição)
# - Obs: em caso de erro deve retornar um JSON contendo 'erro': 'error message'. 

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



    
