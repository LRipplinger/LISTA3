def verificar_soma_menor():
    # Solicita ao usuário os três valores
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))
    
    # Verifica se a soma de A + B é menor que A + C
    if a + b < a + c:
        print("A soma de A + B é menor que A + C.")
    else:
        print("A soma de A + B não é menor que A + C.")

# Chama a função principal
verificar_soma_menor()
