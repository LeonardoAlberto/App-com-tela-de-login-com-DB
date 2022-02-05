from PyQt5 import uic, QtWidgets  # Interface
import sqlite3        # Banco de Dados


def chama_segunda_tela():  # Tela de login primario
    primeira_tela.label4.setText("")
    nome_usuario = primeira_tela.lineEdit.text()  # inputs
    senha = primeira_tela.lineEdit_2.text()  # inputs
    banco = sqlite3.connect('banco_cadastro.db')  # arquivo DataBase
    cursor = banco.cursor()
    try:
        cursor.execute("SELECT senha FROM cadastro WHERE login ='{}'".format(nome_usuario))  # Verificando senha e login
        senha_bd = cursor.fetchall()
        banco.close()
    except:
        print("Error inesperado")

    if senha == senha_bd[0][0]:
        primeira_tela.close()
        segunda_tela.show()
    else:
        primeira_tela.label4.setText('Login ou senha incorretas')


def abre_tela_cadastro():
    tela_cadastro.show()


def cadastrar():  # Interface da tela de cadastro
    nome = tela_cadastro.lineEdit.text()
    login = tela_cadastro.lineEdit_2.text()
    senha = tela_cadastro.lineEdit_3.text()
    c_senha = tela_cadastro.lineEdit_4.text()

    if senha == c_senha:  # Verificando se as duas senhas sao iguais para continuar
        try:
            banco = sqlite3.connect('banco_cadastro.db')  # Conexao com banco de dados
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text,login text,senha text)") # Criando login/senha
            cursor.execute("INSERT INTO cadastro VALUES ('" + nome + "','" + login + "','" + senha + "')")

            banco.commit()
            banco.close()
            tela_cadastro.label.setText("Usuario cadastrado com sucesso")

        except:
            print("Erro ao inserir os dados: ")
    else:
        tela_cadastro.label.setText("As senhas digitadas estão diferentes")


app = QtWidgets.QApplication([])
primeira_tela = uic.loadUi("login.ui")
segunda_tela = uic.loadUi("segunda_tela.ui")
tela_cadastro = uic.loadUi("tela_cadastro.ui")
primeira_tela.pushButton.clicked.connect(chama_segunda_tela)
primeira_tela.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
primeira_tela.pushButton_2.clicked.connect(abre_tela_cadastro)
tela_cadastro.pushButton.clicked.connect(cadastrar)

primeira_tela.show()
app.exec()
