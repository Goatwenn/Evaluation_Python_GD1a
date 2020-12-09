# ----- Import
import random
from colorama import init
init()
from colorama import Fore, Back, Style


# ----- Definition
def lettre_aleatoire(tableau,lettre):
    for i in range (0,23):
        alea = random.randint(0,25)
        tableau[i] = lettres[alea]
    return(tableau)


# ----- Code Variables

#Var_Basiques
conditon_victoir = 0

#Var_Listes
lettres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

mot_mystere_1 = ['c','o','m','p','t','e']
mot_mystere_2 = ['c','o','m','p','t','e']
mot_mystere_3 = ['c','o','m','p','t','e']
mot_mystere_4 = ['c','o','m','p','t','e']

tableau = ['c','o','m','p','t','e','c','o','m','p','t','e','c','o','m','p','t','e','c','o','m','p','t','e']
#tableau =|Ligne 1                |Ligne 2                |Ligne 3                |Ligne 4                |

lettre_aleatoire(tableau,lettres)

# ----- Code Principal

while (conditon_victoir == 0):
    

    resultat_1 = 0
    resultat_2 = 0
    resultat_3 = 0
    resultat_4 = 0
 
    choix_position = int(input(" ou aller :"))
    nouvelle_lettre = str(input(" remplacer par :"))
    tableau[choix_position] = str(nouvelle_lettre)
 
    #verif
    for i in range(0,24):
        if(i > 0 and i <= 6):
            for j in range(0,6):
                if (tableau[i-1] == mot_mystere_1[j]):
                    resultat_1 = resultat_1 + 1
        if(i > 6 and i <= 12):
                for j in range(0,6):
                    if (tableau[i-1] == mot_mystere_2[j]):
                        resultat_2 = resultat_2 + 1
        if(i > 12 and i <= 18):
                for j in range(0,6):
                    if (tableau[i-1] == mot_mystere_3[j]):
                        resultat_3 = resultat_3 + 1     
        if(i > 17 and i <= 24):
                for j in range(0,6):
                    if (tableau[i] == mot_mystere_4[j]):
                        resultat_4 = resultat_4 + 1
    # ----- Affichage
    for ligne in range(0,4):
                for colone in range(0,6):
                    print(Fore.BLUE + Style.BRIGHT + " ",tableau[colone+6*ligne], end='')
                print(Style.RESET_ALL)
    print(resultat_1,resultat_2,resultat_3,resultat_4)



# ----- Code Fin
input()
