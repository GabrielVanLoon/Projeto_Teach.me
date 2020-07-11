from src.dao.usuario import *

# Model: lida com as regras de negócio e validações
# - Tipos de validação: valores obrigatórios, tipos de dados, formatos válidos ou
#   inválidos e outras validações lógicas necessárias (Ex: validações de consistencia como instrutor local == intrutos proposta)
# - Realiza as chamadas aos DAOS e à outros Models se necessário.
# Obs: validações que não forem possíveis serem realizadas no momento devem ser anotadas com @TODO 

class UsuarioModel:

    def cadastrar(self, nome_usuario='', email='', senha ='', nome='', sobrenome='', foto='', eh_instrutor=False):
        
        # 1ª parte - Validação de dados 
        if (nome_usuario == ''):
            raise Exception('Mensagem de erro da merda que aconteceu')
        
        # 2ª parte - validação lógica
        # @TODO: verificar se username existe como classname >> 

        try:
            UsuarioDAO().insert(nome_usuario, email, senha, nome, sobrenome, foto, eh_instrutor)
        except:
            raise Exception('Ocorreu um erro ao inserir os dados')

        return  