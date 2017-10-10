largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

x = y = 1

while y <= altura:
    while x <= largura:

        if (y == 1 or y == altura) or (x == 1 or x == largura):
            print('#', end="")
        else:
            print(' ', end="")

        x = x + 1
    print()
    y = y + 1
    x = 1