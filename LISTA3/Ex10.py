import random

def simular_lancamento_de_dados(numero_faces):
    if numero_faces not in [4, 6, 8, 10, 12, 16]:
        print("Número de faces inválido. Escolha entre 4, 6, 8, 10, 12 ou 16.")
        return

    resultado = random.randint(1, numero_faces)
    print("O resultado do lançamento de um dado de", numero_faces, "faces é:", resultado)

# Solicita ao usuário o número de faces do dado
numero_faces = int(input("Digite o número de faces do dado (4, 6, 8, 10, 12 ou 16): "))

# Chama a função para simular o lançamento de dados
simular_lancamento_de_dados(numero_faces)
