gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

compras_acima_3000 = 0

for gasto in gastos:
  
    if gasto > 3000:
        compras_acima_3000 += 1 

total_compras = len(gastos)
porcentagem = (compras_acima_3000 / total_compras) * 100

print(f"Quantidade de compras acima de R$ 3000: {compras_acima_3000}")
print(f"Porcentagem em relação ao total: {porcentagem:.1f}%")
