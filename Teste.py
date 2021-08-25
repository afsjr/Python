import time
import random as rnd

jogo = ['pedra', 'papel', 'tesoura']

escolha = int(input('Escolha sua opção\n[0] Pedra\n[1] Papel\n[2] Tesoura\n ---> '))
computador = rnd.randint(0, 2)
#print(jogo[computador] + ' X ' + jogo[escolha])
print('='*20)
time.sleep(1)
print('Pedra')
time.sleep(1)
print('Papel')
time.sleep(1)
print('Tesoura')
print('='*20)
time.sleep(1)

if computador == escolha:  # empate para todos
    print(f'Computador jogou {jogo[computador]}')
    print(f'Você jogou jogou {jogo[escolha]}')
    print('Empatou !!!! ')
elif computador == 0 and escolha == 1:  # computador pedra
    print(f'Computador jogou {jogo[computador]}')
    print(f'Você jogou jogou {jogo[escolha]}')
    print(' Você Ganhou ! uhuuuullll ')
elif computador == 0 and escolha == 2:  # computador pedra
    print(f'Computador jogou {jogo[computador]}')
    print(f'Você jogou jogou {jogo[escolha]}')
    print(' Computador ganhou ! :\'( ')

elif computador == 1 and escolha == 0:  # computador papel
    print(f'Computador jogou {jogo[computador]}')
    print(f'Você jogou jogou {jogo[escolha]}')
    print('computador ganhou !!! ')
elif computador == 1 and escolha == 2:  # computador papel
    print(f'Computador jogou {jogo[computador]}')
    print(f'Você jogou jogou {jogo[escolha]}')
    print(' Computador ganhou ! :\'( ')

elif computador == 2 and escolha == 0:  # computador tesoura
    print(f'Computador jogou {jogo[computador]}')
    print(f'Você jogou jogou {jogo[escolha]}')
    print(' Você Ganhou ! uhuuuullll ')
elif computador == 2 and escolha == 1:  # computador tesoura
    print(f'Computador jogou {jogo[computador]}')
    print(f'Você jogou jogou {jogo[escolha]}')
    print(' Computador ganhou ! :\'( ')
