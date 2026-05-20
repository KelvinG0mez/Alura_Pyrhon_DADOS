votos_marca = {
    "Design 1": 1334,
    "Design 2": 982,
    "Design 3": 1751,
    "Design 4": 210,
    "Design 5": 1811
}

total_votos = sum(votos_marca.values())
vencedor = max(votos_marca, key=votos_marca.get)
votos_vencedor = votos_marca[vencedor]
porcentagem = (votos_vencedor / total_votos) * 100

print(f"Design vencedor: {vencedor}")
print(f"Quantidade de votos: {votos_vencedor}")
print(f"Porcentagem de votos recebidos: {porcentagem:.2f}%")
