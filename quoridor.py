"""Module de la classe Quoridor

Classes:
    * Quoridor - Classe pour encapsuler le jeu Quoridor.
"""
from copy import deepcopy

from quoridor_error import QuoridorError

from graphe import construire_graphe

# TODO : créer le fichier quoridor_error.py contenant la classe QuoridorError


class Quoridor:
    """Classe pour encapsuler le jeu Quoridor.

    Vous ne devez pas créer d'autre attributs pour votre classe.

    Attributes:
        état (dict): état du jeu tenu à jour.
    """

    def __init__(self, joueurs, murs=None):
        """Constructeur de la classe Quoridor.

        Initialise une partie de Quoridor avec les joueurs et les murs spécifiés,
        en s'assurant de faire une copie profonde de tout ce qui a besoin d'être copié.

        Appel la méthode `vérification` pour valider les données et assigne
        ce qu'elle retourne à l'attribut `self.état`.

        Cette méthode ne devrait pas être modifiée.

        Args:
            joueurs (List): un itérable de deux joueurs dont le premier est toujours celui qui
                débute la partie.
            murs (Dict, optionnel): Un dictionnaire contenant une clé 'horizontaux' associée à
                la liste des positions [x, y] des murs horizontaux, et une clé 'verticaux'
                associée à la liste des positions [x, y] des murs verticaux.
        """
        self.état = deepcopy(self.vérification(joueurs, murs))

    def vérification(self, joueurs, murs):
        """Vérification d'initialisation d'une instance de la classe Quoridor.

        Valide les données arguments de construction de l'instance et retourne
        l'état si valide.

        Args:
            joueurs (List): un itérable de deux joueurs dont le premier est toujours celui qui
                débute la partie.
            murs (Dict, optionnel): Un dictionnaire contenant une clé 'horizontaux' associée à
                la liste des positions [x, y] des murs horizontaux, et une clé 'verticaux'
                associée à la liste des positions [x, y] des murs verticaux.
        Returns:
            Dict: Une copie de l'état actuel du jeu sous la forme d'un dictionnaire.
                  Notez que les positions doivent être sous forme de list [x, y] uniquement.
        Raises:
            QuoridorError: L'argument 'joueurs' n'est pas itérable.
            QuoridorError: L'itérable de joueurs en contient un nombre différent de deux.
            QuoridorError: Le nombre de murs qu'un joueur peut placer est plus grand que 10,
                            ou négatif.
            QuoridorError: La position d'un joueur est invalide.
            QuoridorError: L'argument 'murs' n'est pas un dictionnaire lorsque présent.
            QuoridorError: Le total des murs placés et plaçables n'est pas égal à 20.
            QuoridorError: La position d'un mur est invalide.
        """
        pass

    def formater_légende(self):
        a = self["joueurs"][0]["murs"]
        b = self["joueurs"][0]["nom"]
        c= 9-len(b)
        d = self["joueurs"][1]["murs"]
        e = self["joueurs"][1]["nom"]
        f= 9-len(e)
        return f"Légende:\n1={b},{c*' '}murs={a*'|'}\n2={e},{f*' '}murs={d*'|'}\n"
        pass

    def formater_damier(self):
        damier = '   -----------------------------------\n'
        for a in range(9):
            damier += str(9 - a) + " | .   .   .   .   .   .   .   .   . |\n" + \
                "  |                                   |\n"
        damier = damier[:719]
        damier += "--|-----------------------------------\n"
        damier += "  | 1   2   3   4   5   6   7   8   9\n"

        damier = damier[:(39 + (self["joueurs"][0].get("pos")[0]) * 4) \
            + 80 * (9-self["joueurs"][0].get("pos")[1])] \
            + "1" + damier[(39 + (self["joueurs"][0].get("pos")[0]) * 4) + \
                80 * (9 - self["joueurs"][0].get("pos")[1]) + 1:]
        damier = damier[:(39 + (self["joueurs"][1].get("pos")[0]) * 4) +\
             80 * (9-self["joueurs"][1].get("pos")[1])] \
            + "2" + damier[(39 + (self["joueurs"][1].get("pos")[0]) * 4) +\
                80 * (9 - self["joueurs"][1].get("pos")[1]) + 1:]

        MH = self["murs"].get("horizontaux")
        MV = self["murs"].get("verticaux")

        for b in MH:
            MH_x = '-------'
            damier = damier[:(78 + (b[0]) * 4) + 80 * (9 - b[1])] +\
                MH_x + damier[(80 + (b[0]) * 4) + 80 * (9 - b[1]) + 5:]

        for c in MV:
            MV_y = '|'
            damier = damier[:(39 + (c[0] * 4 + 4) + 80 * (9 - c[1]) - 6)] + MV_y \
                + damier[(39 + (c[0] * 4 + 3) + 80 * (9 - c[1])) - 4:]
            damier = damier[:((c[0] * 4 + 3) + 80 * (9 - c[1]) - 6)] + MV_y \
                + damier[((c[0] * 4 + 3) + 80 * (9 - c[1])) - 5:]
            damier = damier[:-40 + ((c[0] * 4 + 3) + 80 * (9 - c[1]) - 6)] \
                + MV_y + damier[-40 + ((c[0] * 4 + 3) + 80 * (9 - c[1])) - 5:]
        return damier 
        pass

    def __str__(self):
        return formater_légende(self) + formater_damier(self)
        pass

    def état_courant(self):
        """Produire l'état actuel du jeu.

        Cette méthode ne doit pas être modifiée.

        Returns:
            Dict: Une copie de l'état actuel du jeu sous la forme d'un dictionnaire.
                  Notez que les positions doivent être sous forme de liste [x, y] uniquement.
        """
        return deepcopy(self.état)

    def est_terminée(self):
        if self[parties]["gagnant"]:
            return self[parties]["gagnant"]
        else:
            False
        pass

    def récupérer_le_coup(self, joueur):
        """Récupérer le coup

        Notez que seul 2 questions devrait être posée à l'utilisateur.

        Notez aussi que cette méthode ne devrait pas modifier l'état du jeu.

        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).

        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: Le type de coup est invalide.
            QuoridorError: La position est invalide (en dehors du damier).

        Returns:
            tuple: Un tuple composé d'un type de coup et de la position.
               Le type de coup est une chaîne de caractères.
               La position est une liste de 2 entier [x, y].
        """
        pass

    def déplacer_jeton(self, joueur, position):
        """Déplace un jeton.

        Pour le joueur spécifié, déplacer son jeton à la position spécifiée.

        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).
            position (List[int, int]): La liste [x, y] de la position du jeton (1<=x<=9 et 1<=y<=9).

        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: La position est invalide (en dehors du damier).
            QuoridorError: La position est invalide pour l'état actuel du jeu.
        """
        pass

    def placer_un_mur(self, joueur, position, orientation):
        """Placer un mur.

        Pour le joueur spécifié, placer un mur à la position spécifiée.

        Args:
            joueur (int): le numéro du joueur (1 ou 2).
            position (List[int, int]): la liste [x, y] de la position du mur.
            orientation (str): l'orientation du mur ('horizontal' ou 'vertical').

        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: Un mur occupe déjà cette position.
            QuoridorError: La position est invalide pour cette orientation.
            QuoridorError: Le joueur a déjà placé tous ses murs.
        """
        pass

    def jouer_le_coup(self, joueur):
        """Jouer un coup automatique pour un joueur.

        Pour le joueur spécifié, jouer automatiquement son meilleur coup pour l'état actuel
        de la partie. Ce coup est soit le déplacement de son jeton, soit le placement d'un
        mur horizontal ou vertical.

        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).

        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: La partie est déjà terminée.

        Returns:
            Tuple[str, List[int, int]]: Un tuple composé du type et de la position du coup joué.
        """
        pass
