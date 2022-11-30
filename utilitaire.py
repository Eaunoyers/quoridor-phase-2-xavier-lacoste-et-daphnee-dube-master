"""Module de fonctions utilitaires pour le jeu jeu Quoridor

Functions:
    * analyser_commande - Génère un interpréteur de commande.
"""

import argparse


def analyser_commande():
    """Génère un interpréteur de commande.

    Returns:
        Namespace: Un objet Namespace tel que retourné par `parser.parse_args()`.
                    Cet objet a trois attributs: « idul » représentant l'idul
                    du joueur, « parties » qui est un booléen `True`/`False`
                    et « local » qui est un booléen `True`/`False`.
    """
    parser = argparse.ArgumentParser()

    # Complétez le code ici

    return parser.parse_args()


def formater_les_parties(parties):
    """Formater une liste de parties
    L'ordre rester exactement la même que ce qui est passé en paramètre.
    Args:
        parties (list): Liste des parties
    Returns:
        str: Représentation des parties
    """
    pass
