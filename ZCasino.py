import os
import random
from math import ceil

continuer_parti = True

cash = input("la valeur que vous voulez investir : ")
cash = int(cash)

while continuer_parti:

    chiffrechoisie = input("Sur quel chiffre misez-vous : ")
    chiffrechoisie = int(chiffrechoisie)

    if 0 <= chiffrechoisie < 50:
        print("votre chiffre est enregistrer")
    else:
        chiffrechoisie = input("entre 0 et 49 svp : ")

    mamise = input("Combien voulez-vous miser sur votre chiffre ? ")
    mamise = int(mamise)

    if cash < mamise:
        mamise = input("Vous manquez de fond! inscrire un plus petit montant svp : ")
    print("rien ne va plus les jeux sont fait!")

    chiffrecasino = random.randrange(50)
    print("la roulette est tombé sur le chiffre : ", chiffrecasino)

    if chiffrechoisie == chiffrecasino:
        cash += (3 * mamise)
        Print("Felicitation vous avez gagnez : ", 3 * mamise)
    elif (chiffrechoisie % 2 == 0) and (chiffrecasino % 2 == 0):
        cash += (0.5 * mamise)
        print("Felicitation vous-gagnez : ", 0.5 * mamise)
    else:
        cash -= mamise
        print("Desolez vous avez perdu : ", mamise)

    print("votre solde est à : ", cash)

    if 0 >= cash:
        print("vous avez pu assez de fond")
        continuer_parti = False

    else:
        print("vous avez : ", cash, "$")
        quitter = input("voulez vous quittez le casino ? (oui ou non) : ")

        if quitter == "oui":
            print("merci et a la prochaine fois!")
            continuer_parti = False

os.system("pause")
