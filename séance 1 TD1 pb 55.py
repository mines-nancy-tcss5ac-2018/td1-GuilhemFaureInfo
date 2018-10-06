def Inverse(chaine):###inverse une chaine de caract�re
    
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
        ###on initialise k � i plus le nombre i renvers� (1�re it�ration du processus de "reverse and add"), et le nombre d'it�rations est donc initialis� � 1
        k = i + int(Inverse(str(i)))
        N_iterations = 1
        
        ###condition: que l'on obtienne pas un palindrome � l'issus d'une it�ration du processus de "reverse and add" et que le nombre d'it�rations ne d�passe pas 50
        while N_iterations <= 50 and not palindrome(k) :
            k = k + int(Inverse(str(k)))
            N_iterations += 1
            
        ###si apr�s 51 it�rations (>50) aucun palindrome n'a �t� obtenu, alors on consid�re que le nombre de d�part pour le processus est de Lychrel    
        if N_iterations == 51: 
            N_Lychrel += 1
        
    return N_Lychrel

print(solve(10000))