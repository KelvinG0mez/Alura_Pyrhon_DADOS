dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

valida = False

if mes >= 1 and mes <= 12:
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        if dia >= 1 and dia <= 31:
            valida = True
    elif mes in [4, 6, 9, 11]:
        if dia >= 1 and dia <= 30:
            valida = True
    elif mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if dia >= 1 and dia <= 29:
                valida = True
        else:
            if dia >= 1 and dia <= 28:
                valida = True

if valida:
    print("Data válida")
else:
    print("Data inválida")
