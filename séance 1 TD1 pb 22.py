def ListePrenomsTriee(): ###retourne la liste des prénoms, dans l'ordre alphabétique, constituée à partir de la liste de prénoms donnée dans le document p022_names.text
        ### NB: les éléments de cette liste sont de la forme '"PRENOM"'
        
        textePrenoms= open('p022_names.txt', 'r')
        listePrenoms=[]    
        
        for ligne in textePrenoms:
                listePrenoms+=ligne.split(',')
                
        return sorted(listePrenoms)  

def score(prenom, listePrenomsTriee): ###cette fonction retourne le "score" -comme défini dans l'énoncé du problème 22- associé à un prénom (prenom est une chaine de caractères)

        prenomAvecGuillemets='"'+prenom+'"' ###ajout de guillemets en début et en fin du prénom pour que la synthaxe coïncide avec celle des éléments de la liste de prénoms créée
        alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        Somme=0
        N=0
        
        ###détermination du numéro de la position du prénom "prenom" dans la liste des prénoms triée
        for i in range(len(listePrenomsTriee)):
                if prenomAvecGuillemets==listePrenomsTriee[i]:
                        N=i+1 ###car ici, par convention, on choisit d'indicé le premier élément de la liste des prénoms à 1 et non à 0
        
        ###calcul de la somme des numéro d'apparition dans l'alphabet des lettres qui compose le prénom "prenom"
        for e in prenom:
                for i in range(len(alphabet)):
                        if e==alphabet[i]:
                                Somme+=i+1 ###on considère que la première lettre de l'alphabet n'est pas associé au numéro 0 ma
        return N*Somme      
        
def solve():
        
        Somme=0
        listePrenomsTriee=ListePrenomsTriee()

        for name in listePrenomsTriee:
                Somme+=score(name[1:len(name)-1],listePrenomsTriee) ###score prend en argument 'PRENOM' et non '"PRENOM"', ce pourquoi on l'applique à name[1:len(name)-1]
        
        return Somme
        
assert score('COLIN',ListePrenomsTriee()) == 49714

print(solve())