def converter_real_para_euro(valor, cotacao_real_euro):
    return valor / cotacao_real_euro

def converter_real_para_dolar(valor, cotacao_real_dolar):
    return valor / cotacao_real_dolar

def converter_euro_para_dolar(valor, cotacao_euro_dolar):
    return valor * cotacao_euro_dolar

def converter_euro_para_real(valor, cotacao_real_euro):
    return valor * cotacao_real_euro

def converter_dolar_para_euro(valor, cotacao_dolar_euro):
    return valor * cotacao_dolar_euro

def converter_dolar_para_real(valor, cotacao_real_dolar):
    return valor * cotacao_real_dolar

# Solicita ao usuário as cotações
cotacao_real_dolar = float(input("Digite a cotação do dólar em relação ao real: "))
cotacao_real_euro = float(input("Digite a cotação do euro em relação ao real: "))
cotacao_euro_dolar = float(input("Digite a cotação do euro em relação ao dólar: "))

# Apresenta o menu
print("\nMenu:")
print("1) Converter de Real para Euro")
print("2) Converter de Real para Dólar")
print("3) Converter de Euro para Dólar")
print("4) Converter de Euro para Real")
print("5) Converter de Dólar para Euro")
print("6) Converter de Dólar para Real")

# Solicita ao usuário a opção desejada
opcao = int(input("Escolha uma opção (1-6): "))

# Verifica a opção selecionada e realiza a conversão
if opcao == 1:
    valor = float(input("Digite o valor em reais: "))
    resultado = converter_real_para_euro(valor, cotacao_real_euro)
    print("Valor convertido para Euro:", resultado)
elif opcao == 2:
    valor = float(input("Digite o valor em reais: "))
    resultado = converter_real_para_dolar(valor, cotacao_real_dolar)
    print("Valor convertido para Dólar:", resultado)
elif opcao == 3:
    valor = float(input("Digite o valor em euros: "))
    resultado = converter_euro_para_dolar(valor, cotacao_euro_dolar)
    print("Valor convertido para Dólar:", resultado)
elif opcao == 4:
    valor = float(input("Digite o valor em euros: "))
    resultado = converter_euro_para_real(valor, cotacao_real_euro)
    print("Valor convertido para Real:", resultado)
elif opcao == 5:
    valor = float(input("Digite o valor em dólares: "))
    resultado = converter_dolar_para_euro(valor, 1/cotacao_euro_dolar)
    print("Valor convertido para Euro:", resultado)
elif opcao == 6:
    valor = float(input("Digite o valor em dólares: "))
    resultado = converter_dolar_para_real(valor, 1/cotacao_real_dolar)
    print("Valor convertido para Real:", resultado)
else:
    print("Opção inválida. Por favor, escolha uma opção de 1 a 6.")
