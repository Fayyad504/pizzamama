import time
print(f" {0})oeuf a la coque {3}minutes")
print(f"{1})oeuf mollet {6}minutes")
print(f"{2})oeuf dur {9}minutes ")

choix=input("quel est votre choix: ") 

duree=0
if choix==1:
     duree=3
if choix==2:
     duree=6
if choix==3:
    duree=9

while True:
    for i in range(5):
        time.sleep(1)
        duree -= 1
        print(".",end="",flush=True)
        if duree<=0:
            break
    sec=duree*60
    print(f" temps restant:{duree:02d} :{sec:02d}", end="",flush=True)
print("votre repas est près")