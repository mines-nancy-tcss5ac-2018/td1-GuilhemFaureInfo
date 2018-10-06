def Inverse(chaine):###inverse une chaine de caractère
    
    chaineInv=''
    l = len(chaine)
    
    for i in range(l):
        chaineInv += chaine[l-1-i]
        
    return chaineInv

def palindrome(N):###retourne True si N est un nombre palindrome, False sinon
    
    Nstring = str(N)
    
    return Nstring == Inverse(Nstring)

def solve(n):
    N_Lychrel = 0
    
    for i in range(n+1):
        ###on initialise k à i plus le nombre i renversé (1ère itération du processus de "reverse and add"), et le nombre d'itérations est donc initialisé à 1
        k = i + int(Inverse(str(i)))
        N_iterations = 1
        
        ###condition: que l'on obtienne pas un palindrome à l'issus d'une itération du processus de "reverse and add" et que le nombre d'itérations ne dépasse pas 50
        while N_iterations <= 50 and not palindrome(k) :
            k = k + int(Inverse(str(k)))
            N_iterations += 1
            
        ###si après 51 itérations (>50) aucun palindrome n'a été obtenu, alors on considère que le nombre de départ pour le processus est de Lychrel    
        if N_iterations == 51: 
            N_Lychrel += 1
        
    return N_Lychrel

print(solve(10000))