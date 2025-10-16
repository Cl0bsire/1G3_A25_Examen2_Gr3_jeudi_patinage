# test_notation.py
# Tests unitaires pour le module notation.py

import pytest
from notation import *

# -----------------------------
# TODO : Tests unitaires pour valider_notes()
# -----------------------------
@pytest.mark.parametrize("notes, resultat_attendu", [
    ([3,2,1,2,3,3,2,2,3], True),
    ([0,1,2,0,1,2,1,1,1], True),
    ([-3,-2,-2,-2,-2,-1,-1,-1,0], True),
    ([1,2,3], False),
    ([-4,2,1,2,3,3,2,2,3], False)
])
def test_valider_notes(notes, resultat_attendu):
    # Arrange
    # Act
    resultat = valider_notes(notes)

    # Assert
    assert resultat == resultat_attendu


# -----------------------------
# TODO : Tests unitaires pour calculer_points()
# -----------------------------
@pytest.mark.parametrize("vbase, notes, resultat_attendu", [
    (3.2, [3,2,1,2,3,3,2,2,3], 5.628571428571428),
    (2.5, [0,1,2,0,1,2,1,1,1], 3.5),
    (1.0, [-3,-2,-2,-2,-2,-1,-1,-1,0], -0.5714285714285714),
    (3.0, [1,2,3], 0),
    (2.5, [-4,2,1,2,3,3,2,2,4], 0)
])

def test_calculer_points(vbase, notes, resultat_attendu):
    # Arrange
    # Act
    resultat = calculer_points(vbase, notes)

    # Assert
    assert resultat == resultat_attendu