import datetime

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

try:
    datetime.date(ano, mes, dia)
    print("Data válida")
  
except ValueError:
    print("Data inválida")
