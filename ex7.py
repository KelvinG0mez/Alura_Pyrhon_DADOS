bacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
crescimento = []

for i in range(1, len(bacterias)):
  
    atual = bacterias[i]
    passada = bacterias[i - 1]
    pct = 100 * (atual - passada) / passada
    crescimento.append(round(pct, 2))

print(crescimento)
