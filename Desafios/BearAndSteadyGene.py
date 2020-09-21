gen = input('Digite o gene para a analise: ')

n_gen = len(gen) // 4
n_gen_g = len(gen) // 4
n_gen_t = len(gen) // 4
n_gen_c = len(gen) // 4
n_gen_a = len(gen) // 4

counter = 0

counter_g = 0
counter_a = 0
counter_c = 0
counter_t = 0

if len(gen) % 4 != 0:
    print('O tamanho do gene deve ser divisivel por 4.')
else:
    for i in range(len(gen)):
        if gen[i] != 'G' and gen[i] != 'C' and gen[i] != 'T' and gen[i] != 'A':
            print('Gene com erro!')
            break

    for i in range(len(gen)):
        if gen[i] == 'G':
            counter_g += 1
        if gen[i] == 'T':
            counter_t += 1
        if gen[i] == 'A':
            counter_a += 1
        if gen[i] == 'C':
            counter_c += 1

    
    # if counter_g > n_gen:
    #     counter += 1
    
    # if counter_t > n_gen:
    #     counter += 1

    # if counter_c > n_gen:
    #     counter += 1

    # if counter_a > n_gen:
    #     counter += 1




    if counter_g < n_gen :
        n_gen_a -= counter_g
        counter += n_gen_g
    
    if counter_t < n_gen :
        n_gen_t -= counter_t
        counter += n_gen_t

    if counter_c < n_gen :
        n_gen_c -= counter_c
        counter += n_gen_c

    if counter_a < n_gen :
        n_gen_a -= counter_a
        counter += n_gen_a

    


print(counter)

            


