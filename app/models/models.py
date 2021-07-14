import mysql.connector as connect

connection = connect.connect(host = 'localhost', database = 'db_agenda', user = 'root', password = 'jean6032')
cursor = connection.cursor()

class Buscador():

    def getIdUser(nome, senha):
        try:
            cursor.execute('''SELECT idUSUARIO 
                          FROM usuario WHERE NOME = '{}' and SENHA = '{}';'''.format(nome, senha))
            return cursor.fetchone()[0]
        except:
            return 0

    def getContatos(forma, valor, nome):
        if forma == 'TODOS':
            cursor.execute('''SELECT contato.NOME, contato.NUMERO, contato.EMAIL FROM db_agenda.contato, db_agenda.usuario WHERE contato.idUSUARIO = usuario.idUSUARIO and usuario.NOME = '{}';'''.format(nome))

        else:
            cursor.execute('''SELECT contato.NOME, contato.NUMERO, contato.EMAIL FROM db_agenda.contato, db_agenda.usuario WHERE contato.idUSUARIO = usuario.idUSUARIO and usuario.NOME = '{}' and contato.{} = '{}';'''.format(nome, forma, valor))

        contatos = cursor.fetchall()
        return list(contatos)

    def deletar(nome, senha, contato):
        cursor.execute('''DELETE FROM db_agenda.contato WHERE (contato.NOME = '{}') and (usuario.Nome = '{}');'''.format(contato), nome)


class Usuario():
    def __init__(self, userName, senha):
        self.nome = userName
        self.senha = senha
        self.contatos = []

    def getNome(self):
        return self.nome

    def getSenha(self):
        return self.senha

    def getId(self):
        cursor.execute()

    def setNome(self, newName):
        self.nome = newName


    def saveUser(self):
        cursor.execute('''INSERT INTO usuario (NOME, SENHA) VALUES ('{}', '{}');'''.format(self.getNome(), self.getSenha()))
        connection.commit()

class Contato():
    def __init__(self, user_id, nome, numero, email):
        self.user_id = user_id
        self.nome = nome
        self.numero = numero
        self.email = email

    def getUser_id(self):
        return self.user_id

    def getNome(self):
        return self.nome

    def getNumero(self):
        return self.numero

    def getEmail(self):
        return self.email

    def getId(self):
        cursor.execute()

    def saveContato(self):
        cursor.execute('''INSERT INTO db_agenda.contato (idUSUARIO, NUMERO, EMAIL, NOME) 
                       VALUES ('{}', '{}', '{}', '{}');'''.format(self.getUser_id(), self.getNumero(), self.getEmail(), self.getNome()))
        connection.commit()

class GrupoContatos():
    def __init__(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome

