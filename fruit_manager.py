import json


def ouvrir_inventaire(path="inventaire.json"):
    with open(path, mode="r", encoding="utf-8") as file:
        inventaire = json.load(file)
    return inventaire


def ecrire_inventaire(inventaire, path="inventaire.json"):
    with open(path, mode="w", encoding="utf-8") as file:
        json.dump(inventaire, file, indent=4, ensure_ascii=False)


def afficher_inventaire(inventaire):
    print("Inventaire actuel de la plantation :")
    for fruit, quantite in inventaire.items():
        print(f"- {fruit.capitalize()} : {quantite} unités")


def recolter(inventaire, fruit, quantite):
    inventaire[fruit] = inventaire.get(fruit, 0) + quantite
    print(f"✅ récolté {quantite} {fruit} supplémentaires ")


def vendre(inventaire, fruit, quantite):
    inventaire[fruit] = inventaire.get(fruit, 0) - quantite
    print(f"✅ vendu {quantite} {fruit} supplémentaires ")


if __name__ == "__main__":

    inventaire = ouvrir_inventaire()
    afficher_inventaire(inventaire)
    recolter(inventaire, "bananes", 10)
    afficher_inventaire(inventaire)
    vendre(inventaire, "bananes", 5)
    afficher_inventaire(inventaire)
