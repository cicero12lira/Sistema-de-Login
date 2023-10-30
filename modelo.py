# modelo.py
from peewee import *
import bcrypt

db = SqliteDatabase('usuarios.db')

class Usuario(Model):
    nome = CharField()
    email = CharField(unique=True)
    senha = CharField()

    class Meta:
        database = db

    @staticmethod
    def criar_usuario(nome, email, senha_plana):
        senha_hash = bcrypt.hashpw(senha_plana.encode('utf-8'), bcrypt.gensalt())
        return Usuario.create(nome=nome, email=email, senha=senha_hash.decode('utf-8'))
