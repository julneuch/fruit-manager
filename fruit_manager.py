import json


def ouvrir_inventaire(path="data/inventaire.json"):
    with open(path, mode="r", encoding="utf-8") as file:
        inventaire = json.load(file)
    return inventaire


def ecrire_inventaire(inventaire, path="data/inventaire.json"):
    with open(path, mode="w", encoding="utf-8") as file:
        json.dump(inventaire, file, indent=4, ensure_ascii=False)


def ouvrir_prix(path="data/prix.json"):
    with open(path, mode="r", encoding="utf-8") as file:
        prix = json.load(file)
    return prix


def ouvrir_tresorerie(path="data/tresorerie.txt"):
    with open(path, mode="r", encoding="utf-8") as file:
        tresorerie = int(file.readline())
    return tresorerie


def ecrire_tresorerie(tresorerie, path="data/tresorerie.txt"):
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
    inventaire[fruit] = inventaire.get(fruit, 0) - quantite
    tresorerie += prix.get(fruit, 0) * quantite
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
