ids = []
doces = 0
amargos = 0

for i in range(10):
    id_produto = int(input(f"Digite o ID do {i+1}º produto: "))
    ids.append(id_produto)

for id_produto in ids:
  
    if id_produto % 2 == 0:
        doces += 1
    else:
        amargos += 1

print(f"Quantidade de produtos doces (IDs pares): {doces}")
print(f"Quantidade de produtos amargos (IDs ímpares): {amargos}")
