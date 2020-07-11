
# Data Access Object: lida com a comunicação com o banco de dados
# - Os dados recebidos devem ser considerados como devidamente validados.
# - query: SQL utilizado para comunicar com o banco de dados.
# - nenhuma outra preocupação por enquanto.

class UsuarioDAO:

    def insert(self, nome_usuario='', email='', senha ='', nome='', sobrenome='', foto='', eh_instrutor=False):
        query = 'INSERT INTO usuario (colunas) VALUE (dados)'
        return True



