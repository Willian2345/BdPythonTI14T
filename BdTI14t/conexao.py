import  mysql.connector #Elemento que faz a conexão com o banco de dados
from mysql.connector import  errorcode
class conexao:
    def __init__(self):
        pass

    def conectar(self):
        try:
            self.db_connection = mysql.connector.connect(host='localhost',
                                                         user='root',
                                                         password='',
                                                         database='bdTI14TPython')
            print('Conectado com Sucesso!')
            return self.db_connection
        except mysql.connector.Error as erro:
            if erro.errno == errorcode.ER_BAD_DB_ERROR: # caso o banco de dados não exista
                print("Banco de Dados não existe\n Erro: {} ".format(erro))
            elif  erro.errno == errorcode.ER_ACESS_DENIED_ERROR:#Há um erro de usuário
                print("Nome de usuário ou senha inválida! \n Erro: {}".format(erro))

            else:
                print("Erro")

        else:
            self.db_connection.close()#fechando a conexão com o banco de dados
