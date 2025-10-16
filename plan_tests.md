PLAN DE TESTS – Système de notation patinage artistique

TODO : Compléter le plan de tests suivants : 

| # | Description du test          | vbase | notes                       | Résultat attendu (valider_notes) | Résultat obtenu (valider_notes) | Résultat attendu (calculer_points) | Résultat obtenu (calculer_points) |
|---|------------------------------|-------|-----------------------------|----------------------------------|---------------------------------|------------------------------------|-----------------------------------|
| 1 | Cas normal                   | 3.2   | [3,2,1,2,3,3,2,2,3]         | True                             | True                            | 5.628571428571428                  | 5.628571428571428                 |
| 2 | Plusieurs max/min identiques | 2.5   | [0,1,2,0,1,2,1,1,1]         | True                             | True                            | 3.5                                | 3.5                               |
| 3 | Notes négatives              | 1.0   | [-3,-2,-2,-2,-2,-1,-1,-1,0] | True                             | True                            | -0.5714285714285714                | -0.5714285714285714               |
| 4 | Liste invalide (taille)      | 3.0   | [1,2,3]                     | False                            | False                           | Erreur                             | Erreur                            |
| 5 | Valeurs hors bornes          | 2.5   | [-4,2,1,2,3,3,2,2,4]        | False                            | False                           | Erreur                             | Erreur                            |

