import bibliotheque as bib


def afficher_menu():
    # Affichage du menu principal de l'application
    print("\n           GESTION DE BIBLIOTHÈQUE PERSONNELLE          ")
    print("1. Afficher tous les livres")
    print("2. Ajouter un livre")
    print("3. Supprimer un livre")
    print("4. Rechercher un livre")
    print("5. Marquer un livre comme lu")
    print("6. Afficher les livres lus")
    print("7. Afficher les livres non lus")
    print("8. Trier les livres")
    print("9. Quitter")
    return input("\nChoisissez une option (1-9): ")


def main():
    """Fonction principale du programme"""
    # Charger la bibliothèque au démarrage
    bib.charger_bibliotheque()
    # Boucle principale du programme
    while True:
        choix = afficher_menu()
        if choix == "1":
            bib.afficher_tous_livres()
        elif choix == "2":
            bib.ajouter_livre()
        elif choix == "3":
            bib.supprimer_livre()
        elif choix == "4":
            bib.rechercher_livre()
        elif choix == "5":
            bib.marquer_comme_lu()
        elif choix == "6":
            bib.afficher_livres_par_statut(lu=True)
        elif choix == "7":
            bib.afficher_livres_par_statut(lu=False)
        elif choix == "8":
            bib.trier_livres()
        elif choix == "9":
            bib.sauvegarder_bibliotheque()
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez réessayer.")


# Point d'entrée du programme
if __name__ == "__main__":
    main()