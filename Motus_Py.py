# ----- Import
import random
from colorama import init
init()
from colorama import Fore, Back, Style


# ----- Definition



# ----- Code Principal


choix = input(" choisisez une lettre :")
mot_mystere = ['c','o','m','p','t','e']
position = 0

for i in range(0,6):
    if (mot_mystere[i] == choix):
        position = (i+1)

print(position)
    
    
    
    
    
    
input()