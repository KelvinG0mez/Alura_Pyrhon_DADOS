gabarito = ["D", "A", "C", "B", "A", "D", "C", "C", "A", "B"]
respostas_aluno = []
nota = 0

for i in range(10):
    resposta = input(f"Digite a resposta da questão {i+1} (A, B, C ou D): ").strip().upper()
    respostas_aluno.append(resposta)

for i in range(10):
  
    if respostas_aluno[i] == gabarito[i]:
        nota += 1

print(f"Nota final do(a) aluno(a): {nota} de 10")
