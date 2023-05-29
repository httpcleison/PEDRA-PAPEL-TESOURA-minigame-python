game = True
pontoJogador = 0
pontoBot = 0

while game==True:
    import random
    bot = ['pedra', 'papel', 'tesoura']
    Varrandom = random.randint(0,2)
    bot2 = bot[Varrandom]
    jogador = input("\nSua vez: ")
    print("IA: "+bot2)
    
    if bot2 == 'tesoura' and jogador == 'papel' or bot2 == 'pedra' and jogador == 'tesoura' or bot2 == 'papel' and jogador == 'pedra':
        print('IA ganhou!!')
        pontoBot += 1
        
    elif bot2 == 'tesoura' and jogador == 'tesoura' or bot2 == 'pedra' and jogador == 'pedra' or bot2 == 'papel' and jogador == 'papel':
        print("Empate.")
        
    else:
        print("Voce ganhou!!!!")
        pontoJogador +=1
        
    print("IA: ", pontoBot, "YOU: ", pontoJogador)