def verificar_divisibilidade_por_3(numero):
    if numero % 3 == 0:
        print(numero, "é divisível por 3.")
    else:
        print(numero, "não é divisível por 3.")

# Solicita ao usuário um número inteiro
numero = int(input("Digite um número inteiro: "))

# Chama a função para verificar a divisibilidade por 3
verificar_divisibilidade_por_3(numero)
