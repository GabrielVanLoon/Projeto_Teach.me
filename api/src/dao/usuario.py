
class UsuarioDAO:

    def insert(self, nome_usuario='', email='', senha ='', nome='', sobrenome='', foto='', eh_instrutor=False):
        query = 'INSERT INTO usuario (colunas) VALUE (dados)'
        print('Inserindo novo usuário no servidor...')
        return True



