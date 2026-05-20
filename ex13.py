salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
dicionario_abonos = {}
total_gastos = 0
cont_minimo = 0
maior_abono = 0

for salario in salarios:
  
    abono = salario * 0.10
  
    if abono < 200:
        abono = 200
        cont_minimo += 1
    
    dicionario_abonos[salario] = abono
    total_gastos += abono
    
    if abono > maior_abono:
        maior_abono = abono

print(f"Total de gastos com o abono: R$ {total_gastos:.2f}")
print(f"Quantidade de colaboradores que receberam o abono mínimo: {cont_minimo}")
print(f"Maior valor de abono fornecido: R$ {maior_abono:.2f}")
