def ListePrenomsTriee(): ###retourne la liste des pr�noms, dans l'ordre alphab�tique, constitu�e � partir de la liste de pr�noms donn�e dans le document p022_names.text
        ### NB: les �l�ments de cette liste sont de la forme '"PRENOM"'
        
        textePrenoms= open('p022_names.txt', 'r')
        listePrenoms=[]    
        
        for ligne in textePrenoms:
                listePrenoms+=ligne.split(',')
                
        return sorted(listePrenoms)  

def score(prenom, listePrenomsTriee): ###cette fonction retourne le "score" -comme d�fini dans l'�nonc� du probl�me 22- associ� � un pr�nom (prenom est une chaine de caract�res)

        prenomAvecGuillemets='"'+prenom+'"' ###ajout de guillemets en d�but et en fin du pr�nom pour que la synthaxe co�ncide avec celle des �l�ments de la liste de pr�noms cr��e
        alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        Somme=0
        N=0
        
        ###d�termination du num�ro de la position du pr�nom "prenom" dans la liste des pr�noms tri�e
        for i in range(len(listePrenomsTriee)):
                if prenomAvecGuillemets==listePrenomsTriee[i]:
                        N=i+1 ###car ici, par convention, on choisit d'indic� le premier �l�ment de la liste des pr�noms � 1 et non � 0
        
        ###calcul de la somme des num�ro d'apparition dans l'alphabet des lettres qui compose le pr�nom "prenom"
        for e in prenom:
                for i in range(len(alphabet)):
                        if e==alphabet[i]:
                                Somme+=i+1 ###on consid�re que la premi�re lettre de l'alphabet n'est pas associ� au num�ro 0 ma
        return N*Somme      
        
def solve():
        
        Somme=0
        listePrenomsTriee=ListePrenomsTriee()

        for name in listePrenomsTriee:
                Somme+=score(name[1:len(name)-1],listePrenomsTriee) ###score prend en argument 'PRENOM' et non '"PRENOM"', ce pourquoi on l'applique � name[1:len(name)-1]
        
        return Somme
        
assert score('COLIN',ListePrenomsTriee()) == 49714

print(solve())