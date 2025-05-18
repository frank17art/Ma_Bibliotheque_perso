# Module des fonctions utilitaires pour le programme de bibliothèque.

def generer_id(bibliotheque):
    # Génère un ID unique pour un nouveau livre
    if not bibliotheque:
        return 1
    # Trouver l'ID le plus élevé et ajouter 1
    ids = [livre["ID"] for livre in bibliotheque]
    return max(ids) + 1


def trouver_livre_par_id(bibliotheque, id_livre):
    # Trouver un livre par son ID
    for livre in bibliotheque:
        if livre["ID"] == id_livre:
            return livre
    return None


def rechercher_par_mot_cle(bibliotheque, mot_cle):
    # Recherche des livres par mot-clé dans le titre ou l'auteur
    resultats = []
    mot_cle = mot_cle.lower()
    for livre in bibliotheque:
        if mot_cle in livre["Titre"].lower() or mot_cle in livre["Auteur"].lower():
            resultats.append(livre)
    return resultats


def trier_livres_par_critere(bibliotheque, choix):
    # Trie les livres selon un critère spécifique
    livres_tries = bibliotheque.copy()
    if choix == "1":
        # Tri par année
        livres_tries.sort(key=lambda livre: livre["Année"])
        return livres_tries
    elif choix == "2":
        # Tri par auteur
        livres_tries.sort(key=lambda livre: livre["Auteur"])
        return livres_tries
    elif choix == "3":
        # Tri par note
        def cle_tri_note(livre):
            return livre["Note"] if livre["Note"] is not None else float('inf')
        livres_tries.sort(key=cle_tri_note)
        return livres_tries
    else:
        print("Option invalide.")
        return None