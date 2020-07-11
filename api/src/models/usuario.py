from src.dao.usuario import *


class UsuarioModel:

    def cadastrar(self, nome_usuario='', email='', senha ='', nome='', sobrenome='', foto='', eh_instrutor=False):
        
        if (nome_usuario == ''):
            raise Exception('Mensagem de erro da merda que aconteceu')
        
        try:
            UsuarioDAO().insert(nome_usuario, email, senha, nome, sobrenome, foto, eh_instrutor)
        except:
            raise Exception('Ocorreu um erro ao inserir os dados')

        return  