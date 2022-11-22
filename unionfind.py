pai = {}
rank = {}

def create_set(x):
    pai[x] = x
    rank[x] = 1

def find(x):
    p = pai.get(x)
    if p is None:
       return None  # o elemento nao existe!!

    if p == x:
        return x

    representante = find(p)

    # PATH COMPRESSION
    pai[x] = representante

    return representante


def find_nao_recursivo(x):
    p = pai.get(x)
    if p is None:
       return None  # o elemento nao existe!!

    corrente = x
    while p != corrente:
       corrente = p
       p = pai.get(p)
 
    # PATH COMPRESSION
    representante = p
    corrente = x
    while corrente != representante:
        pai[corrente] = representante
        corrente = pai[corrente]

    return representante

def union(x, y):
    repx = find(x)
    repy = find(y)
    if repx == repy:
       return  # ja estao no mesmo set!!

    rankrepx = rank[repx]
    rankrepy = rank[repy]
    
    # UNION BY RANK
    if rankrepy > rankrepx:
        pai[repx] = repy
    else:
        pai[repy] = repx
        if rankrepx == rankrepy:
            rank[repx] += 1    






# MAIN!!!

create_set(5)
create_set(7)

print find(5)
print find(6)
print find(7)

union(5,7)
print "\n"

create_set(6)



create_set(10)
create_set(11)
create_set(12)
union(11,12)
union(11,10)


union(6, 10)
print "union(6,10)"
print "find(6) -->", find(6)
print "find(10) -->", find(10)

union(6,5)
print "union(6,5)"
print "find(6) -->", find(6)
print "find(10) -->", find(10)
print "find(5) -->", find(5) 
print "find(7) -->", find(7)
print "find(12) -->", find(12)



