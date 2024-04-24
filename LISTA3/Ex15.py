def calcular_valor_produto(preco, opcao_pagamento):
    if opcao_pagamento == 1:
        return preco - (preco * 0.15)  # À vista em dinheiro, 15% de desconto
    elif opcao_pagamento == 2:
        return preco - (preco * 0.10)  # À vista no cartão de crédito, 10% de desconto
    elif opcao_pagamento == 3:
        return preco  # Em duas vezes, preço normal de etiqueta sem juros
    elif opcao_pagamento == 4:
        return preco * 1.10  # Em três vezes, preço normal de etiqueta mais juros de 10%
    else:
        return None  # Opção inválida

# Solicita ao usuário o preço do produto
preco_produto = float(input("Digite o preço do produto: "))

# Solicita ao usuário a opção de pagamento
opcao_pagamento = int(input("Escolha a condição de pagamento (1-4): "))

# Calcula o valor a ser pago pelo produto
valor_final = calcular_valor_produto(preco_produto, opcao_pagamento)

# Exibe o valor final a ser pago pelo produto
if valor_final is not None:
    print("O valor a ser pago pelo produto é R$", valor_final)
else:
    print("Opção de pagamento inválida.")
