import json
import os
import datetime

DATA_DIR = "data"
PRIX_PATH = os.path.join(DATA_DIR, "prix.json")
INVENTAIRE_PATH = os.path.join(DATA_DIR, "inventaire.json")
TRESORERIE_PATH = os.path.join(DATA_DIR, "tresorerie.txt")
TRESORERIE_EVOL_PATH = os.path.join(DATA_DIR, "tresorerie.json")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)


def ouvrir_inventaire(path=INVENTAIRE_PATH):
    if not os.path.exists(path):
        inventaire = {
            "bananes": 150,
            "mangues": 200,
            "ananas": 50,
            "noix de coco": 60,
            "papayes": 20,
        }
        with open(path, mode="w", encoding="utf-8") as file:
            json.dump(inventaire, file, indent=4, ensure_ascii=False)
    with open(path, mode="r", encoding="utf-8") as file:
        inventaire = json.load(file)
    return inventaire


def ouvrir_tresorerie_evolution(path=TRESORERIE_EVOL_PATH):
    if not os.path.exists(path):
        evol = []
        with open(path, mode="w", encoding="utf-8") as file:
            json.dump(evol, file, indent=4, ensure_ascii=False)
    with open(path, mode="r", encoding="utf-8") as file:
        evol = json.load(file)
    return evol


def ecrire_inventaire(inventaire, path=INVENTAIRE_PATH):
    with open(path, mode="w", encoding="utf-8") as file:
        json.dump(inventaire, file, indent=4, ensure_ascii=False)


def ecrire_tresorerie_evolution(tresorerie, path=TRESORERIE_EVOL_PATH):
    histo = []
    if os.path.exists(path):
        with open(path, mode="r", encoding="utf-8") as file:
            try:
                histo = json.load(file)
            except:
                histo = []
    histo.append(
        {"timestamp": datetime.datetime.now().isoformat(), "tresorerie": tresorerie}
    )
    with open(path, mode="w", encoding="utf-8") as file:
        json.dump(histo, file, indent=4, ensure_ascii=False)


def ouvrir_prix(path=PRIX_PATH):
    if not os.path.exists(path):
        prix = {
            "bananes": 8,
            "mangues": 15,
            "ananas": 6,
            "noix de coco": 7,
            "papayes": 11,
        }
        with open(path, mode="w", encoding="utf-8") as file:
            json.dump(prix, file, indent=4, ensure_ascii=False)
    with open(path, mode="r", encoding="utf-8") as file:
        prix = json.load(file)
    return prix


def ouvrir_tresorerie(path=TRESORERIE_PATH):
    if not os.path.exists(path):
        tresorerie = 1000
        with open(path, mode="w", encoding="utf-8") as file:
            file.write(str(tresorerie))
    with open(path, mode="r", encoding="utf-8") as file:
        tresorerie = int(file.readline())
    return tresorerie


def ecrire_tresorerie(tresorerie, path=TRESORERIE_PATH):
    with open(path, mode="w", encoding="utf-8") as file:
        file.write(str(tresorerie))


def afficher_tresorerie(tresorerie):
    
    print(f"💰 Trésrorie : {tresorerie}")


def afficher_inventaire(inventaire):
    print("Inventaire actuel de la plantation :")
    for fruit, quantite in inventaire.items():
        print(f"- {fruit.capitalize()} : {quantite} unités")


def recolter(inventaire, fruit, quantite):
    inventaire[fruit] = inventaire.get(fruit, 0) + quantite
    print(f"✅ récolté {quantite} {fruit} supplémentaires ")


def vendre(inventaire, fruit, quantite, tresorerie, prix):
    if inventaire.get(fruit, 0) < quantite:
        quantite = inventaire.get(fruit, 0)
    inventaire[fruit] = inventaire.get(fruit, 0) - quantite
    tresorerie += prix.get(fruit, 0) * quantite
    ecrire_tresorerie_evolution(tresorerie)
    print(f"💰 vendu {quantite} {fruit} supplémentaires ")
    return (inventaire, tresorerie)


if __name__ == "__main__":

    inventaire = ouvrir_inventaire()
    tresorerie = ouvrir_tresorerie()
    prix = ouvrir_prix()
    afficher_tresorerie(tresorerie)
    afficher_inventaire(inventaire)
    recolter(inventaire, "bananes", 10)
    afficher_inventaire(inventaire)
    inventaire, tresorerie = vendre(inventaire, "bananes", 5, tresorerie, prix)
    ecrire_inventaire(inventaire)
    ecrire_tresorerie(tresorerie)
    afficher_inventaire(inventaire)
    afficher_tresorerie(tresorerie)
