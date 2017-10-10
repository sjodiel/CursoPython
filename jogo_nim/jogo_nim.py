jogo = 0
 
def computador_escolhe_jogada(n, m):
     
    # Vez do computador:
    #print("O computador começa!\n")
     
    # Pode retirar todas as peças?
    if n <= m:
         
        # Retira todas as peças e ganha o jogo:
        print(" ")
        return n
     
    else:
        print("\nO computador começa!")
        # Verifica se é possível deixar uma quantia múltipla de m+1:
        quantia = n % (m+1)
         
        if quantia > 0:
            return quantia
         
        # Não é, então tire m peças:
        return m
 
def usuario_escolhe_jogada(n, m):
     
    # Vez do usuário:
    print("\nVoce começa!\n")
     
    # Define o número de peças do usuário:
    jogada = 0
     
    # Enquanto o número não for válido
    while jogada == 0:
         
        # Solicita ao usuário quantas peças irá tirar:
        jogada = int(input("Quantas peças você vai tirar? "))
 
        # Condições: jogada < n, jogada < m, jogada > 0
        if jogada > n or jogada < 1 or jogada > m:
             
            # Valor inválido, continue solicitando ao usuário:
            print("\nOops! Jogada inválida! Tente de novo.\n")
            jogada = 0
             
    # Número de peças válido, então retorne-o:
    return jogada
 
def partida():
     
    print(" ")
     
    # Solicita ao usuário os valores de n e m:
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
     
    # Define uma variável para controlar a vez do computador:
    is_computer_turn = True
     
    # Decide quem iniciará o jogo:
    if n % (m+1) == 0: is_computer_turn = False
     
    # Execute enquanto houver peças no jogo:
    while n > 0:
         
        if is_computer_turn:
            jogada = computador_escolhe_jogada(n, m)
            is_computer_turn = False
            if jogada <= 1:
                print("\nO computador tirou uma peça")
            else:
                print("\nO computador tirou {} peças.".format(jogada))
        else:
            jogada = usuario_escolhe_jogada(n, m)
            is_computer_turn = True
            if jogada <= 1:
                print("Você tirou uma peça.") 
            else:
                print("Você tirou {} peças.".format(jogada)) 

             
        # Retira as peças do jogo:
        n = n - jogada
         
        # Mostra o estado atual do jogo:
        if (n==1):
            print("Agora resta apenas uma peça no tabuleiro.")
        elif (n!=0 or n>1):
            print("Agora restam {} peças no tabuleiro.".format(n))
        
    # Fim de jogo, verifica quem ganhou:
    if is_computer_turn:
        print("Fim do jogo! Você ganhou!")
        return 1
    else:
        print("Fim do jogo! O computador ganhou!")
        return 0
     
def campeonato():
     
    # Pontuações:
    usuario = 0
    computador = 0
     
    # Executa 3 vezes:
    rodada=1
    for _ in range(3):

        print("\n **** Rodada {} ****".format(rodada))
         
        # Executa a partida:
        vencedor = partida()
         
        # Verifica o resultado, somando a pontuação:
        if vencedor == 1:
            # Usuário venceu:
            usuario = usuario + 1
            rodada += 1
        else:
            # Computador venceu:
            computador = computador + 1
            rodada += 1
    
    # Exibe o placar final:
    print("\n**** Final do campeonato! ****")
    print("\nPlacar: Você  {} x {}  Computador".format(usuario, computador))
     
     
# Enquanto não for uma opção válida:
while jogo == 0:
     
    # Menu de opções:
    print("\nBem-vindo ao jogo do NIM! Escolha:")
    print(" ")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
     
    # Solicita a opção ao usuário:
    jogo = int(input())
    print(" ")
 
    # Decide o tipo de jogo:
    if jogo == 1:
        print("Voce escolheu partida isolada!")
        partida()
        break
    if jogo == 2:
        print("Voce escolheu um campeonato!")
        campeonato()
        break
    else:
        print("Opção inválida!")
        jogo = 0