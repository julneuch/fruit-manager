inventaire = {
    "bananes": 120,
    "mangues": 85,
    "ananas": 45,
    "noix de coco": 60,
    "papayes": 30,
}


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
    afficher_inventaire(inventaire)
    recolter(inventaire, "bananes", 10)
    afficher_inventaire(inventaire)
    vendre(inventaire, "bananes", 5)
    afficher_inventaire(inventaire)
