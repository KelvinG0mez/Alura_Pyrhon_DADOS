limite = int(input("Digite um número: "))
primos = []

for num in range(2, limite + 1):
    e_primo = True
    
    for i in range(2, int(num ** 0.5) + 1):
        
        if num % i == 0:
            e_primo = False
            break
            
    if e_primo:
        primos.append(num)

print(primos)
