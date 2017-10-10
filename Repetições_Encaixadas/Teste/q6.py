altura = 5
linha = 1
while linha <= altura:
    print("*", end = "") #errado print("*")
    coluna = 2
    while coluna < altura: 
        if linha == 1 or linha == altura:
            print("*", end = "") #print("*") modificado 
        else:
            print(end = " ")
        coluna = coluna + 1
    print("*") # errado print("*", end = "")
    linha = linha + 1