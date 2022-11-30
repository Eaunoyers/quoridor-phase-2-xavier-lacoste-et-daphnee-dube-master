"""Jeu Quoridor

Ce programme permet de joueur au jeu Quoridor.
"""
from api import débuter_partie, jouer_coup, lister_parties
from quoridor import Quoridor
from utilitaire import analyser_commande, formater_les_parties

# Mettre ici votre secret récupéré depuis le site de PAX
SECRET = ""

if __name__ == "__main__":
    args = analyser_commande()
    if args.parties:
        parties = lister_parties(args.idul, SECRET)
        print(formater_les_parties(parties))
    else:
        if args.local:
            # Implémenter la boucle pour jouer contre votre bot en local
            pass
        else:
            # Implémenter la boucle pour jouer contre le bot du serveur
            pass
