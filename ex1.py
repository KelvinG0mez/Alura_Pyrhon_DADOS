gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

soma_total = sum(gastos)

quantidade_meses = len(gastos)

media_gastos = soma_total / quantidade_meses

print(f"A média de gastos da empresa foi de: R$ {media_gastos:.2f}")
