
if __name__ == '__main__':

  with open('dados_elecao.txt','r') as pleito:
    urna = pleito.read() # tratando os dados
    nova_urna = urna.replace('\n',',').split(',') # transforma em vetor separado por vírgulas

    winner = []
    cand1 = nova_urna.count('Khan')
    winner.append(cand1)
    cand2 = nova_urna.count('Correy')
    winner.append(cand2)
    cand3 = nova_urna.count('Li')
    winner.append(cand3)
    cand4 = nova_urna.count("O'Tooley")
    winner.append(cand4)
    total = cand1 + cand2 + cand3 + cand4
    candidatos = ["Khan","Correy","Li","O'Tooley"]
    maior_indice = max(winner)
    ganhou = candidatos[winner.index(maior_indice)]

  with open('resultado.txt','w') as pleito:


    pleito.write('RESULTADOS ELEITORAIS\n')
    pleito.write('-'*30)
    pleito.write(f'\n Total de Votos : {total}\n')
    pleito.write('-'*30)
    pleito.write(f'\nKhan :{cand1*100/total:.1f} %\t ({cand1})')
    pleito.write(f'\nCorrey :{cand2*100/total:.1f} %\t ({cand2})')
    pleito.write(f'\nLi :{cand3*100/total:.1f} %\t\t ({cand3})')
    pleito.write(f"\nO'Tooley :{cand4*100/total:.1f} % ({cand4})\n")
    pleito.write('-'*30)
    pleito.write(f'\nO vencedor foi {ganhou}!!! \n')
    pleito.write('-'*30)

