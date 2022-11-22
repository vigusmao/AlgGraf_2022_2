from time import time
import sys

VALOR = 0
PESO = 1

memo = {}

# entrada: 
#  - lista de tuplas (valor, peso)
#  - max_idx: indica ate que item podemos olhar
#  - capac: capacidade da mochila
#           
# saida: o valor otimo para a mochila
# 
def mochila(itens, capac):
    memo.clear()
    return mochila_rec(itens, 
                       len(itens) - 1,
                       capac)

def mochila_rec(itens, max_idx, capac):
    if max_idx < 0:
        return 0

    problem_id = (max_idx, capac)
    result_from_memo = memo.get(problem_id)
    if result_from_memo is not None:
        return result_from_memo

    valor_ultimo = itens[max_idx][VALOR] 
    peso_ultimo = itens[max_idx][PESO]
    
    mochila_com_ultimo = 0
    if capac >= peso_ultimo:  # cabe o ultimo?
        mochila_com_ultimo = (valor_ultimo + \
            mochila_rec(itens, 
                        max_idx - 1,
                        capac - peso_ultimo))

    mochila_sem_ultimo = mochila_rec(itens,
                                     max_idx - 1,
                                     capac)

    otimo = max(mochila_sem_ultimo,
                mochila_com_ultimo)

    memo[problem_id] = otimo

    return otimo




# MAIN!!

N_MAX = 40000
sys.setrecursionlimit(N_MAX + 10)


for N in range(1, N_MAX + 1):
    
    itens = [(1,1)] * N

    start = time()
    result = mochila(itens, N)
    duration = time() - start
    
    print result
    print duration





