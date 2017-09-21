n = int(input("Digite um número inteiro: "))
soma = 0
while n!=0:
    digito = n % 10
    n = n // 10
    soma += digito

print(soma)