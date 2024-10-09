def hello(n):
    if(n < 0):
        return
    
    print("bonjour",n)
    hello(n-2)

    
hello(4)

def somme(a,b):

    if a >= b:
        return a
    else:
        s = somme(a,b-1) + b
        return s
    
s = somme(1,10)

print(s)


def facto_rec(n):

    if n == 0:
        return 1
    
    else :
        return n * facto_rec(n-1)

f = facto_rec(5)
print(f)


def min_tab(T,index_debut,index_fin):

    if index_debut > index_fin :
        return T[index_fin]

    mini = min_tab(T,index_debut+1,index_fin)
    if mini < T[index_debut]:
        return mini
    else:
        return T[index_debut]
    
t = [5,2,3,1,6,-1,6,7,-2,9]

mini = min_tab(t,0,len(t)-1)
print(mini)
