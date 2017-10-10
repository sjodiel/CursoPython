largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

x = y = 1

while y <= altura:
    while x <= largura:
        print('#', end="")
        x = x + 1
    print()
    y = y + 1
    x = 1