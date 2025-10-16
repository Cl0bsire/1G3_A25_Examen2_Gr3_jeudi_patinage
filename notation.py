# notation.py
# TODO : Version buggée — à corriger après exécution des tests unitaires
# TODO : Mettre des commentaires pour identifier les bugs trouvés et comment vous les avez corrigés.

def valider_notes(notes: list[float]) -> bool:
    """
    Vérifie que la liste de notes contient exactement 9 entiers entre -3 et +3.
    :param notes: liste de notes
    :returns: vrai si la liste et valide, sinon faux.
    """
    if len(notes) < 9:
        return False

    for n in notes:
        if n > 3:
            return False
        elif n < -3:
            return False

    return True


def calculer_points(vbase: float, notes: list[float]) -> float:
    """
    Calcule la note finale d’un mouvement.
    :param vbase: valeur de base de la note
    :param notes: liste de notes
    :returns: valeur de la note finale
    """
    if valider_notes(notes) == True:


        note_max = max(notes)
        note_min = min(notes)
        notes.remove(note_max)
        notes.remove(note_min)

        moyenne = sum(notes) / 7
        total = vbase + moyenne
        return total

    else:
        print("Erreur")
        return 0



