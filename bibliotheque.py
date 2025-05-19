"""
gestion de la bibliothèque.
Contient toutes les fonctions pour manipuler les livres.
"""

import json
import os
import utils

# Variables globales
FICHIER_BIBLIOTHEQUE = "bibliotheque.json"
bibliotheque = []


def charger_bibliotheque():
    """Charge les livres depuis le fichier JSON"""
    global bibliotheque
    # Si le fichier existe, on charge les données
    if os.path.exists(FICHIER_BIBLIOTHEQUE):
        try:
            with open(FICHIER_BIBLIOTHEQUE, "r") as fichier:
                bibliotheque = json.load(fichier)
            print(f"{len(bibliotheque)} livre(s) chargé(s) avec succès!")
        except ValueError:
            print("Erreur lors du chargement du fichier.")
            bibliotheque = []
    else:
        print("Aucun fichier trouvé. Création d'une nouvelle bibliothèque.")
        bibliotheque = []


def sauvegarder_bibliotheque():
    """Sauvegarde les livres dans le fichier JSON"""
    try:
        with open(FICHIER_BIBLIOTHEQUE, "w") as fichier:
            json.dump(bibliotheque, fichier, indent=4)
        print(f"{len(bibliotheque)} livre(s) sauvegardé(s) avec succès!")
    except ValueError:
        print("Erreur lors de la sauvegarde du fichier.")


def afficher_livre(livre):
    """Affiche les informations d'un livre avec un formatage simple"""
    statut = "Lu" if livre["Lu"] else "Non lu"
    note = f"Note: {livre['Note']}/10" if livre["Note"] is not None else "Pas encore noté"
    print(f"\nID: {livre['ID']}")
    print(f"Titre: {livre['Titre']}")
    print(f"Auteur: {livre['Auteur']}")
    print(f"Année: {livre['Année']}")
    print(f"Statut: {statut}")
    if livre["Lu"]:
        print(note)
    print("-" * 30)


def afficher_tous_livres():
    """Affiche tous les livres de la bibliothèque"""
    if not bibliotheque:
        print("La bibliothèque est vide.")
        return
    print("\n===== TOUS LES LIVRES =====")
    for livre in bibliotheque:
        afficher_livre(livre)
    print(f"Total: {len(bibliotheque)} livre(s)")


def ajouter_livre():
    """Ajoute un nouveau livre à la bibliothèque"""
    print("\n===== AJOUTER UN LIVRE =====")
    try:
        titre = input("Titre: ")
        if not titre:
            print("Le titre ne peut pas être vide.")
            return
        auteur = input("Auteur: ")
        if not auteur:
            print("L'auteur ne peut pas être vide.")
            return
        annee_str = input("Année de publication: ")
        try:
            annee = int(annee_str)
            if annee < 0 or annee > 2025:  # Vérification simple
                print("L'année semble invalide.")
                return
        except ValueError:
            print("Veuillez entrer un nombre valide pour l'année.")
            return
        # Création du nouveau livre
        nouveau_livre = {
            "ID": utils.generer_id(bibliotheque),
            "Titre": titre,
            "Auteur": auteur,
            "Année": annee,
            "Lu": False,
            "Note": None
        }
        # Ajout à la bibliothèque
        bibliotheque.append(nouveau_livre)
        print(f"Livre '{titre}'succès de l`ajout {nouveau_livre['ID']}!")
    except Exception as e:
        print(f"Erreur lors de l'ajout du livre: {e}")


def supprimer_livre():
    """Supprime un livre de la bibliothèque par son ID"""
    print("\n===== SUPPRIMER UN LIVRE =====")
    if not bibliotheque:
        print("La bibliothèque est vide.")
        return
    try:
        id_str = input("Entrez l'ID du livre à supprimer: ")
        try:
            id_livre = int(id_str)
        except ValueError:
            print("Veuillez entrer un nombre valide pour l'ID.")
            return
        # Rechercher le livre par ID
        livre_trouve = utils.trouver_livre_par_id(bibliotheque, id_livre)
        if not livre_trouve:
            print(f"Aucun livre trouvé avec l'ID {id_livre}.")
            return
        # Confirmation
        print("\nVous allez supprimer le livre suivant:")
        afficher_livre(livre_trouve)
        confirmation = input("voulez vous suprimer ce livre? (o/n): ")
        if confirmation.lower() == "o":
            bibliotheque.remove(livre_trouve)
            print(f"Livre '{livre_trouve['Titre']}' supprimé avec succès!")
        else:
            print("Suppression annulée.")
    except Exception as e:
        print(f"Erreur lors de la suppression du livre: {e}")


def rechercher_livre():
    """Recherche un livre par mot-clé dans le titre ou l'auteur"""
    print("\n===== RECHERCHER UN LIVRE =====")
    if not bibliotheque:
        print("La bibliothèque est vide.")
        return
    mot_cle = input("Entrez un mot-clé (titre ou auteur): ")
    if not mot_cle:
        print("Veuillez entrer un mot-clé valide.")
        return
    resultats = utils.rechercher_par_mot_cle(bibliotheque, mot_cle)
    if not resultats:
        print(f"Aucun livre trouvé pour '{mot_cle}'.")
    else:
        print(f"\n{len(resultats)} livre(s) trouvé(s) pour '{mot_cle}':")
        for livre in resultats:
            afficher_livre(livre)


def marquer_comme_lu():
    """Marque un livre comme lu et permet d'ajouter une note"""
    print("\n===== MARQUER UN LIVRE COMME LU =====")
    if not bibliotheque:
        print("La bibliothèque est vide.")
        return
    try:
        id_str = input("Entrez l'ID du livre que vous avez lu: ")
        try:
            id_livre = int(id_str)
        except ValueError:
            print("Veuillez entrer un nombre valide pour l'ID.")
            return
        # Rechercher le livre par ID
        livre_trouve = utils.trouver_livre_par_id(bibliotheque, id_livre)
        if not livre_trouve:
            print(f"Aucun livre trouvé avec l'ID {id_livre}.")
            return
        # Marquer comme lu
        livre_trouve["Lu"] = True
        # Ajouter une note
        note_str = input("Donnez une note sur 10 (ou laissez vide):")
        if note_str:
            try:
                note = float(note_str)
                if 0 <= note <= 10:
                    livre_trouve["Note"] = note
                else:
                    print("La note doit être entre 0 et 10.")
            except ValueError:
                print("Veuillez entrer un nombre valide pour la note.")
        print(f"Livre '{livre_trouve['Titre']}' marqué comme lu!")
    except Exception as e:
        print(f"Erreur: {e}")


def afficher_livres_par_statut(lu=True):
    """Affiche les livres lus ou non lus"""
    statut = "lus" if lu else "non lus"
    print(f"\n===== LIVRES {statut.upper()} =====")
    livres_filtres = [livre for livre in bibliotheque if livre["Lu"] == lu]
    if not livres_filtres:
        print(f"Aucun livre {statut} trouvé.")
        return
    for livre in livres_filtres:
        afficher_livre(livre)
    print(f"Total: {len(livres_filtres)} livre(s) {statut}")


def trier_livres():

#Trie et affiche les livres selon différents critères
    print("\n===== TRIER LES LIVRES =====")
    if not bibliotheque:
        print("La bibliothèque est vide.")
        return
    print("Critères de tri:")
    print("1. Par année")
    print("2. Par auteur")
    print("3. Par note")
    choix = input("Choisissez un critère (1-3): ")
    livres_tries = utils.trier_livres_par_critere(bibliotheque, choix)
    if livres_tries:
        critere = ""
        if choix == "1":
            critere = "année"
        elif choix == "2":
            critere = "auteur"
        elif choix == "3":
            critere = "note"
        print(f"\nLivres triés par {critere}:")
        for livre in livres_tries:
            afficher_livre(livre)