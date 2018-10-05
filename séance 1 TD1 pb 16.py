def solve(n):
    N=str(n)  ## je construis un objet de type string avec mon nombre pour pouvoir balayer les lettres (qui correspondent aux chiffres à sommer, mais en type string)
    L=[]
    Somme=0
    ## je balaie les lettres du mot construit précédemment en les convertissant en entiers (car il s'agit de chiffres en type string) et les sommant (le résultat de la somme est stocké dans Somme)
    for i in N:
        Somme+=int(i)
    return Somme

assert solve(2**15)==26

print(solve(2**1000))

###solution alternative###
def solve2(n):
    r=0
    whilen!=0:
        r+=n%10
        n=n//10
    return(r)