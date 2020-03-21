def main():
    h_1 = int(input('Digite qual a hora do inicio do jogo: '))
    m_1 = int(input('Digite em que minuto começou o jogo: '))
    h_2 = int(input('Digite qual hora terminou o jogo: '))
    m_2 = int(input('Digite em que minuto terminou o jogo: '))

    jogo(h_1, m_1, h_2, m_2)


def jogo(h_1, m_1, h_2, m_2):
    h = (h_2 - h_1) - 1 
    m = m_2 - m_1
    h2 = 24 - (h_1 - h_2)
    m2 = m_1 - m_2
        
    if h > 24:
        print('O jogo não pode ter mais que 24h!')
    elif h2 > 24:
        print('O jogo não pode ter mais que 24h!')
    elif h_1 > 24 or h_2 > 24:
        print('oooops, um dia não tem mais que 24h!')
    elif m_1 > 59 or m_2 > 59:
        print('Ocorreu um erro :( não pode-se usar mais que 59 nos minutos!')
    elif h_2 > h_1 and m_2 >= m_1:
        print(f'O jogo tem exatamente {h} horas e {m} minutos')
    elif h_2 > h_1 and m_2 <= m_1:
        print(f'O jogo tem exatamente {h} horas e {m2} minutos')
    elif h_1 > h_2 and m_2 >= m_1:
        print(f'O jogo tem exatamente {h2} horas e {m} minutos')
    elif h_1 > h_2 and m_2 <= m_1:
        print(f'O jogo tem exatamente {h2} horas e {m2} minutos')
    


main()