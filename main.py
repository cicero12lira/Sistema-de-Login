# main.py
from controlador import ControladorUsuario
from vistas import VistaUsuario

def cadastrar():
    nome, email, senha = VistaUsuario.cadastrar_usuario()
    usuario = ControladorUsuario.cadastrar_usuario(nome, email, senha)
    if usuario:
        print(f"Usuário {usuario.nome} cadastrado com sucesso.")
    else:
        print("Erro: Email já cadastrado.")

def autenticar():
    email, senha = VistaUsuario.autenticar_usuario()
    usuario = ControladorUsuario.autenticar_usuario(email, senha)
    if usuario:
        print(f"Bem-vindo, {usuario.nome}!")
    else:
        print("Erro: Email ou senha incorretos.")

if __name__ == "__main__":
    while True:
        print("\n1. Cadastrar\n2. Autenticar\n3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar()
        elif escolha == "2":
            autenticar()
        elif escolha == "3":
            break
