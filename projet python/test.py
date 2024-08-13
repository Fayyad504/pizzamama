# demander nom
"""nom=""
while nom=="":
    nom=input(" quel est votre nom ?")
return nom



# demander age

def demander_age(nom):
    age=0
    while age==0:
        age_str=input("quel est votre age")
        try:
            age=int(age_str)
        except:
            print("veuillez entrez un age convenable")    
    while age<18:
                print("{nom} tu es mineur tu ne peut pas avoir acces anotree a notre site ")    
    else:
        print(f"{nom} tu as {age} ans ")
    return age        

# demander mot de passe
def demander_mot_de_passe(nom):
    mot_de_passe=""
    while not mot_de_passe=="toto":
        mot_de_passe=input("veuillez entrez un mot de passe correcte")
    print(f"{nom} bienvenue")    
nom=demander_nom()
age=demander_age(nom)
if age==18:
    print(f"bienvenue  {nom} tous juste mineur")


mot_de_passe=demander_mot_de_passe(nom)"""


"""NOMBRE_MINIMAL=1
NOMBRE_MAXIMAL=10
NOMBRE_MAGIQUE=random.randint(NOMBRE_MINIMAL,NOMBRE_MAXIMAL)
NB_vie=4
def demander_nombre(x,y):
    nombre_str=0
    while nombre_str == 0:
        nombre=input(f"quel est le nombre magique entre{x} et {y} ")
        try:
            nombre_str=int(nombre)
        except:
            print("veuillez entrez un nombre")
        else:
              if nombre_str >NOMBRE_MAXIMAL or nombre_str< NOMBRE_MINIMAL:
                print("le nombre doit etre compris entre entre 1 et 10")   
                nombre_str=0
    return nombre_str

for i in range(0,NB_vie):
    vies=NB_vie-i
    print("il vous reste {vies} vie")
    while not nombre==NOMBRE_MAGIQUE:
        nombre=demander_nombre(NOMBRE_MINIMAL,NOMBRE_MAXIMAL)
        if int(nombre) == NOMBRE_MAGIQUE:
            print("vous ète fort")
            break
        elif int(nombre) < NOMBRE_MAGIQUE:
            print(f"le nombre magique est plus grand ")
        else:
            print(f"le nombre magique est plus petit il vous reste {vies} vies")"""
import random
NOMBRE_MINIMAL=1
NOMBRE_MAXIMAL=10
NOMBRE_MAGIQUE=random.randint(NOMBRE_MINIMAL,NOMBRE_MAXIMAL)
 

def demander_nombre(x, y):
    nombre_str = 0
    while nombre_str == 0:
        nombre = input(f"quel est le nombre magique entre{x} et {y} ")
        try:
            nombre_str = int(nombre)
        except:
            print("veuillez entrez un nombre")
        else:
            if nombre_str > NOMBRE_MAXIMAL or nombre_str < NOMBRE_MINIMAL:
                print("le nombre doit etre compris entre entre 1 et 10")
                nombre_str = 0
    return nombre_str

nombre=demander_nombre(NOMBRE_MINIMAL,NOMBRE_MAXIMAL)

import random
NOMBRE_MINIMAL=1
NOMBRE_MAXIMAL=10
NOMBRE_MAGIQUE=random.randint(NOMBRE_MINIMAL,NOMBRE_MAXIMAL)
NB_VIE=4  
gagne=False
for i in range(0,NB_VIE):
    vies=NB_VIE-i
    print(f"il vous reste {vies} vie")
    while not nombre == NOMBRE_MAGIQUE:
        nombre = demander_nombre(NOMBRE_MINIMAL, NOMBRE_MAXIMAL)
        if int(nombre) == NOMBRE_MAGIQUE:
            print("vous ète fort")
            gagne=True
            break
        elif int(nombre) < NOMBRE_MAGIQUE:
            print(f"le nombre magique est plus grand ")
        else:
            print(f"le nombre magique est plus petit ")
if not gagne:
    print(f"vous avez perdu le nombre magique etais {NOMBRE_MAGIQUE}")


