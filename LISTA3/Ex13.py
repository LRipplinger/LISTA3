def calcular_media(nota_a, nota_b):
    return (nota_a + nota_b) / 2

def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Recuperação"

def substituir_nota(nota_a, nota_b, substituir):
    if substituir == 'a':
        nova_nota = float(input("Digite a nova nota do Grau A: "))
        return nova_nota, nota_b
    elif substituir == 'b':
        nova_nota = float(input("Digite a nova nota do Grau B: "))
        return nota_a, nova_nota
    else:
        print("Opção inválida.")
        return nota_a, nota_b

# Solicita ao usuário as notas do Grau A e do Grau B
nota_grau_a = float(input("Digite a nota do Grau A: "))
nota_grau_b = float(input("Digite a nota do Grau B: "))

# Calcula a média final
media_final = calcular_media(nota_grau_a, nota_grau_b)

# Verifica se o aluno passou por média ou está em recuperação
situacao = verificar_aprovacao(media_final)

if situacao == "Recuperação":
    print("O aluno está em recuperação.")
    opcao = input("Deseja substituir a nota do Grau A (a) ou do Grau B (b)? ")
    nova_nota_grau_a, nova_nota_grau_b = substituir_nota(nota_grau_a, nota_grau_b, opcao)
    media_final = calcular_media(nova_nota_grau_a, nova_nota_grau_b)

# Verifica a aprovação com a nova média
situacao = verificar_aprovacao(media_final)

# Exibe o resultado final
print("A média final é:", media_final)
print("Situação:", situacao)
