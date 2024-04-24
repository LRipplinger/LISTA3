def determinar_categoria(idade):
    if idade >= 5 and idade <= 7:
        return "Infantil A"
    elif idade >= 8 and idade <= 10:
        return "Infantil B"
    elif idade >= 11 and idade <= 13:
        return "Juvenil A"
    elif idade >= 14 and idade <= 17:
        return "Juvenil B"
    else:
        return "Sênior"

# Solicita ao usuário a idade do nadador
idade_nadador = int(input("Digite a idade do nadador: "))

# Determina e exibe a categoria do nadador
categoria = determinar_categoria(idade_nadador)
print("A categoria do nadador é:", categoria)
