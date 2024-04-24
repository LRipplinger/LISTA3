def dividir_numeros():
    # Solicita ao usuário os dois números
    dividendo = float(input("Digite o dividendo: "))
    divisor = float(input("Digite o divisor: "))
    
    # Verifica se o divisor é diferente de zero
    if divisor != 0:
        resultado = dividendo / divisor
        print("O resultado da divisão é:", resultado)
    else:
        print("Erro: O divisor não pode ser zero.")

# Chama a função principal
dividir_numeros()
