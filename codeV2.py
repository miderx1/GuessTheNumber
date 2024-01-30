import os
import json
import random

def pause(msg ="Enter para continuar.."):
    input(msg)

def jogar(user,dificuldade):
    usuario = user

    dificuldades = {
        'facil' : 100,
        'medio' : 200,
        'dificil' : 300
    }
    numero = random.randint(0,int(dificuldades[dificuldade]+1))
    tentativas = 10

    while tentativas > 0:
        os.system('cls')
        print (" Tentativas: ", tentativas)
        palpite = int(input("\n Digite um numero: "))

        os.system('cls')

        if palpite > 0 and palpite < dificuldades[dificuldade]+1:
            if palpite == numero:
                print("Parabéns, Você acertou. O numero era: ",numero)
                pause()
                usuario['win'] += 1
                return usuario
            
            elif palpite > numero:
                print("O numero é menor que ",palpite)
                pause()

            else:
                print("O numero é maior que ",palpite)
                pause()
        else:
            print("Palpite fora do limite estabelecido!")
            pause()
            continue

        tentativas -= 1

    os.system('cls')
    print("Tentativas esgotadas, o numero sorteado era: ",numero)
    pause()
    usuario['loss'] += 1
    return usuario
    
def menu_jogar(user):
    usuario = {}

    os.system('cls')
    print("Escolha uma das dificuldades abaixo: ")
    print("\n\t Facil(0-100)")
    print("\t Medio(0-200)")
    print("\t Difícil(0-300)")

    escolha = input("Opção: ").lower()

    usuario = jogar(user,escolha)
    return usuario

def menu_logar():   
    usuario = {} 
    while True:
        os.system('cls')
        print("Escolha uma das opções abaixo: ")
        print("\t Logar")
        print("\t Cadastrar")
        print("\t Sair")
        escolha = input("Opção: ").lower()
        os.system('cls')

        if escolha == 'logar':
            login = input("Digite o nome de usuário: ")
            usuario = logar(login) 

            if usuario is not None:
                return usuario
            
        elif escolha == 'cadastrar': 
            login = input("Digite um nome de usuário: ")
            usuario = cadastrar(login) 

            if usuario is not None:
                return usuario
        
        elif escolha == 'sair':
            return None

        else:
            print("Opção Inválida!")
            pause()
            
def logar(user_name):
    usuario = {}

    try:
        with open(f'{user_name}.json', 'r', encoding='utf8') as arquivo:
            usuario = json.load(arquivo)
        
            while True:
                os.system('cls')
                senha = input("Digite a senha: ")

                if usuario['senha'] == senha:
                    print("Logado com sucesso!")
                    pause()
                    return usuario
                else:
                    print("Senha incorreta!")
                    pause()
    except FileNotFoundError:
        print("Usuário não encontrado.")
        pause()
        return None

def cadastrar(user_name):
    os.system('cls')
    usuario = {}
    try:
        with open(f'{user_name}.json', 'r', encoding='utf8') as arquivo:
            print("Usuário já existe.")
            pause()
            return None
    except:
        senha = input("Digite uma senha: ")
        usuario['login'] = user_name
        usuario['senha'] = senha
        usuario['win']   = 0
        usuario['loss']  = 0
        with open(f'{user_name}.json', 'w', encoding='utf8') as arquivo:
            json.dump(usuario,arquivo,ensure_ascii=False,indent=2)

        os.system('cls')
        print("Conta criada com sucesso!")
        pause()

        return usuario
    
def backup(user):
    try:
        with open(f'{user['login']}.json', 'w', encoding='utf8') as arquivo:
                json.dump(user,arquivo,ensure_ascii=False,indent=2)
    except:
        print("Falha ao tentar realizar Backup")
        pause()

while True:

    user = menu_logar()

    if user is not None:
        while True:
            os.system('cls')
            print(f'Usuário: {user['login']}')
            print(f'Vitórias: {user['win']}')
            print(f'Derrotas: {user['loss']}')
            print("\nEscolha uma das opções abaixo: ")
            print("\t jogar")
            print("\t Deslogar")

            escolha = input("Opção: ").lower()

            os.system('cls')

            if escolha == 'jogar':
                user = menu_jogar(user)
            elif escolha == 'deslogar':
                backup(user)
                user = {}
                break
            else:
                print("Opção Inválida!")
                pause("Enter para retornar..")
    else:
        print("Programa Encerrado!")
        pause("Enter para encerrar..")
        break



