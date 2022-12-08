# vertices de 1 a n

EST = 0
ANT = 1

def floyd(matriz, n):
    
    M = [None] # descartamos a linha 0 
    
    # criando matriz p/ k=0 a partir da matriz adj
    for i in range(1, n+1):
        linha = [None] # descartamos a coluna 0
        for j in range(1, n+1):
            linha.append([matriz[i][j], i])
        M.append(linha)

    for linha in M:
        print "\n", linha

    

    for k in range(1, n+1):
        print "\n\n\n\n k =", k

        for i in range(1, n+1):
            if i == k:
                continue
            for j in range(1, n+1):
                if j == k:
                    continue
                if M[i][k][EST] is None or \
                     M[k][j][EST] is None:
                    continue
                if M[i][j][EST] is None or \
                    M[i][k][EST] + M[k][j][EST] < \
                        M[i][j][EST]:
                    M[i][j][EST] = M[i][k][EST] + \
                        M[k][j][EST]
                    M[i][j][ANT] = M[k][j][ANT]

        for linha in M:
            print "\n", linha    

    return M     
                        
## MAIN!!

grafo = [None, \
         [None, 0, 10, 8, None, None],
         [None, None, 0, 1, None, 5],
         [None, None, 5, 0, 2, 10],
         [None, None, None, None, 0, 1],
         [None, None, None, None, None, 0]]

M = floyd(grafo, 5)

for linha in M:
    print linha








