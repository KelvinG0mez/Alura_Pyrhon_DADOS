vendas = {
    "Produto A": [15, 20, 10, 30],
    "Produto B": [20, 15, 25, 10],
    "Produto C": [10, 10, 10, 10]
}

for produto, quantidades in vendas.items():
  
    total_vendas = sum(quantidades)
    print(f"{produto}: {total_vendas} unidades vendidas")
