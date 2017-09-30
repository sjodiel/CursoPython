def e_primo(n):
    primo = 2
    while primo * primo <= n:
        if n % primo == 0:
            return False
        primo = primo + 1
    return True

def maior_primo(n):
    for num in reversed(range(1,n+1)):
        if e_primo(num):
            return num

# testes
print(maior_primo(100))
print(maior_primo(7))