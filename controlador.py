# controlador.py
from modelo import Usuario
import bcrypt

class ControladorUsuario:
    @staticmethod
    def cadastrar_usuario(nome, email, senha):
        try:
            usuario = Usuario.get(Usuario.email == email)
            return None  # Retorna None se o e-mail já existe
        except Usuario.DoesNotExist:
            senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
            novo_usuario = Usuario.create(nome=nome, email=email, senha=senha_hash.decode('utf-8'))
            return novo_usuario

    @staticmethod
    def autenticar_usuario(email, senha):
        try:
            usuario = Usuario.get(Usuario.email == email)
            if bcrypt.checkpw(senha.encode('utf-8'), usuario.senha.encode('utf-8')):
                return usuario
            else:
                return None
        except Usuario.DoesNotExist:
            return None
