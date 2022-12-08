def deep_copy(grafo):
    result = []
    for dict_vizinhos in grafo:
        result.append(dict_vizinhos.copy())
    return result   



# lista_arestas: lista cada aresta 
#                no formato (v, w, c), onde 
# v: origem, w: destino, c: capac
# 
# retorna um grafo no formato lista (end direto)
#    de dicts { vizinho --> capac }
def criar_grafo(n, lista_arestas):
    result = []
    for _ in range(n):
        result.append({})
    for aresta in lista_arestas:
        v, w, c = aresta[0], aresta[1], aresta[2]
        result[v][w] = c
    return result



def obter_gargalo(ca, rede_residual):
    gargalo = rede_residual[ca[0]][ca[1]]

    v = ca[1]    
    for i in range(2, len(ca)):
        prox = ca[i]
        capac = rede_residual[v][prox]
        if capac < gargalo:
            gargalo = capac
        v = prox

    return gargalo



def atualizar_fluxo(ca, gargalo, fluxo):
    v = ca[0]
    for i in range(1, len(ca)):
        prox = ca[i]
        
        novo_fluxo = fluxo.get((v, prox), 0) + \
                     gargalo
        fluxo[(v, prox)] = novo_fluxo

        # tem fluxo reverso?
        fluxo_rev = fluxo.get((prox, v))
        if fluxo_rev is not None:
            if novo_fluxo > fluxo_rev:
                fluxo[(v, prox)] = novo_fluxo - \
                                   fluxo_rev
                del fluxo[(prox, v)]
            elif fluxo_rev > novo_fluxo:
                fluxo[(prox, v)] = fluxo_rev - \
                                   novo_fluxo
                del fluxo[(v, prox)]
            else:
                del fluxo[(v, prox)]
                del fluxo[(prox, v)]
        v = prox


 
def atualizar_rede_residual(grafo, ca, fluxo, rr):
    n = len(grafo)
    s = 0
    t = n-1
    v = ca[0]
    for i in range(1, len(ca)):
        prox = ca[i]

        # atualizar RR
        fluxo_dir = fluxo.get((v, prox), 0)
        fluxo_rev = fluxo.get((prox, v), 0)
        cap_dir = grafo[v].get(prox)
        cap_rev = grafo[prox].get(v)

        if fluxo_dir == 0 and fluxo_rev == 0:
            if cap_dir is not None:
                rr[v][prox] = cap_dir
            if cap_rev is not None:
                rr[prox][v] = cap_rev

        elif fluxo_dir > 0:
            if fluxo_dir == cap_dir:
                rr[v].pop(prox)  # saturada!
            else:
                rr[v][prox] = cap_dir - fluxo_dir
            if v != s and prox != t:
                rr[prox][v] = fluxo_dir
                if cap_rev is not None:
                    rr[prox][v] += cap_rev
 
        elif fluxo_rev > 0:
            if fluxo_rev == cap_rev:
                rr[prox].pop(v)  # saturada!
            else:
                rr[prox][v] = cap_rev - fluxo_rev
            if prox != s and v != t:
                rr[v][prox] = fluxo_rev
                if cap_dir is not None:
                    rr[v][prox] += cap_dir        
        v = prox     


def obter_caminho_aumentante(rr, s, t):
#    print "obter_caminho_aumentante"
#    print "rr", rr

    n = len(rr)

    fila = [s]
    comeco = 0

    pais = [None] * n
    pais[s] = s

    while comeco < len(fila):  # fila nao-vazia
        v = fila[comeco]

#        print "\n\nv", v
#        print "fila", fila
#        print "comeco", comeco
#        print "pais", pais
        
        # visite v
        if v == t:
            break

        for w in rr[v]:
            if pais[w] is None:
                # nunca foi enfileirado
                fila.append(w)
                pais[w] = v
          
        comeco += 1
    
    # end while
     
    caminho = [t]
    pai = pais[t]
    if pai is None:
        return None  # t sem pai --> nao tem ca!

    while pai != s:
        caminho.append(pai)
        pai = pais[pai]
    caminho.append(s)

    return caminho[-1::-1]
    


# grafo: lista de listas de 
#        tuplas (vizinho, capac)
# vertice 0: produtor
# vertice n-1: consumidor
#
# retorna fluxo, F
#     onde fluxo: dict { (v,w) --> fluxo nela }
#          F eh o fluxo maximo na rede
def edmondskarp(grafo):
    n = len(grafo)
    s = 0
    t = n-1

    rede_residual = deep_copy(grafo)
    fluxo = {}
    F = 0    

    caminho = obter_caminho_aumentante(
        rede_residual, s, t)

    while caminho is not None:
        gargalo = obter_gargalo(caminho, 
            rede_residual)
        atualizar_fluxo(caminho, 
                        gargalo, 
                        fluxo)
        F += gargalo
        atualizar_rede_residual(grafo,
                                caminho,
                                fluxo,
                                rede_residual)
        caminho = obter_caminho_aumentante(
            rede_residual, s, t)

    return F, fluxo



## Main!!!
lista_arestas = [(0,1,10),
                 (0,2,8),
                 (1,2,5),
                 (1,4,5),
                 (2,4,10),
                 (2,3,2), 
                 (3,4,1)]
grafo = criar_grafo(5, lista_arestas)
print grafo


F, fluxo = edmondskarp(grafo)

print F

print fluxo















