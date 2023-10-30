# vistas.py
class VistaUsuario:
    @staticmethod
    def cadastrar_usuario():
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        return nome, email, senha

    @staticmethod
    def autenticar_usuario():
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        return email, senha
