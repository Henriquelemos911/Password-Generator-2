import random
import time
import os
import platform

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def tipo_senha():
    print(f"""Sua senha contem:
{comp_senha} caracteres
inclui letras maiusculas: {incluse_maiusculas}
inclui letras minusculas: {incluse_minusculas}
inclui numeros: {incluse_numeros}
inclui caracteres especiais: {incluse_caracteres_especiais}""") 

# conta a quantidade de opcoes ativas.
opcoes = 0 
# comprimento da senha
while True:
    comp_senha = input("Digite o comprimento da senha: ")
    time.sleep(0.5)
    comp_senha = int(comp_senha)
    clear()
# verificar se o comprimento da senha é maior que 8 e menor que 32 caso contrario retornar erro
    if comp_senha < 8 or comp_senha > 32:
        print("\nErro: o comprimento da senha deve ser maior que 8 e menor que 32")
        break
    else:
        print("\nComprimento da senha: ", comp_senha)
# inclusao de letras maiúsculas
    incluse_maiusculas = input("\nIncluir letras maiúsculas? (S/N): ").lower()
    if incluse_maiusculas == "s":
        incluse_maiusculas = "SIM"
        clear()
        print("\nLetras maiúsculas incluídas")
        opcoes += 1
        
        letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    else:
        incluse_maiusculas = "NÃO"
        clear()
        print("\nLetras maiúsculas não incluídas")
        letras_maiusculas = ""
# inclusao de letras minúsculas
    incluse_minusculas = input("\nIncluir letras minúsculas? (S/N): ").lower()
    time.sleep(0.5)
    if incluse_minusculas == "s":
        incluse_minusculas = "SIM"
        clear()
        print("\nLetras minúsculas incluídas")
        opcoes += 1
        letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
    else:
        incluse_minusculas = "NÃO"
        clear()
        print("\nLetras minúsculas não incluídas")
        letras_minusculas = ""
# inclusao de números
    incluse_numeros = input("\nIncluir números? (S/N): ").lower()
    time.sleep(0.5)
    if incluse_numeros == "s":
        incluse_numeros = "SIM"
        clear()
        print("\nNúmeros incluídos")
        opcoes += 1
        numeros = "0123456789"
    else:
        incluse_numeros = "NÃO"
        clear()
        print("\nNúmeros não incluídos")
        numeros = ""
# inclusao de caracteres especiais
    incluse_caracteres_especiais = input("\nIncluir caracteres especiais? (S/N): ").lower()
    time.sleep(0.5)
    if incluse_caracteres_especiais == "s":
        incluse_caracteres_especiais = "SIM"
        clear()
        print("\nCaracteres especiais incluídos")
        opcoes += 1
        caracteres_especiais = "!@#$%&*"
    else:
        incluse_caracteres_especiais = "NÃO"
        clear()
        print("\nCaracteres especiais não incluídos")
        caracteres_especiais = ""
# verificar se existe 2 ou mais opcoes marcadas caso contrario retornar erro
    if opcoes < 2:
        clear()
        print("\nErro: é necessário marcar 2 ou mais opções")
        break
# pergutar quantas senhas devem ser geradas


    tipo_senha()
    time.sleep(0.5)
    qtd_senhas = input("\nQuantas senhas deseja gerar(entre 1 a 20 senhas)? ")
    time.sleep(0.5)
    qtd_senhas = int(qtd_senhas)
    if qtd_senhas <1 or qtd_senhas >20:
        print("\nErro:digite uma quantidade entre 1 a 20 senhas.")
    else:
        print(f"\ngerando {qtd_senhas} senhas aguarde.")
        time.sleep(2)
# gerar senha
    for i in range(qtd_senhas):
        senha = ""
        for i in range(comp_senha):
            senha += random.choice(letras_maiusculas + letras_minusculas + numeros + caracteres_especiais)
# retorna senha gerada
        print("Senha gerada: ", senha)
        
