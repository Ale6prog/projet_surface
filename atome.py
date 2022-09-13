"""Objets représentant un atome."""
import numpy as np
RAYON = {"H": 1.20, "C": 1.70, "N": 1.55, "O": 1.4, "F": 1.47,
         "NA": 2.27, "MG": 1.73, "SI": 2.1, "P": 1.8, "S": 1.8,
         "CL": 1.75, "K": 2.75, "CU": 1.4, "ZN": 1.39, "SE": 1.9,
         "BR": 1.85, "I": 1.98, "MN": 2.05, "AL": 1.84, "FE": 1.94,
         "CA": 2.31, "AG": 2.03}


class Atome:
    """Objet Atome."""

    def __init__(self, numero, residu, coordone, element, nbr):
        """Objet représentant un atome ainsi que ces propirétés.

        Args:
            num (str): Numéro du résidu et de la chaine
            residu (str): Code à 3 lettre du résidu
            coordone (array): Coordonnées du centre
            element (str): Element de l'atome
            nbr (int): Nombre de points par atome
        """
        self.num = numero
        self.residu = residu
        self.coordone = np.array(coordone)
        self.element = element
        self.rayon = 0
        self.set_rayon()
        self.surface = 0
        self.list_position = None
        self.list_occupe = np.array([0 for i in range(nbr)])

    def set_rayon(self):
        """Set le rayon selon son élement."""
        if self.element in RAYON:
            self.rayon = RAYON[self.element]

    def set_list_position(self, pos):
        """Set le array des positions de chaque points.

        Args:
            pos (list): liste des positions des points
        """
        self.list_position = np.array(pos)

    def set_surface(self):
        """Set la surface."""
        self.surface = (((4 * np.pi) / (len(self.list_occupe))) *
                        ((self.rayon+1.4)**2)) * self.compte_libre()

    def compte_libre(self):
        """Compte le nombre de points non enfouie.

        Returns:
            int: Nombre de points libres
        """
        return len(self.list_occupe)-(sum(self.list_occupe))

    def compte_pris(self):
        """Compte le nombre de points enfouie.

        Returns:
            int: Nombre de points enfouie
        """
        return (len(self.list_occupe)) - self.compte_libre(self)

    def set_occupe(self, k):
        """Set une position de la liste comme occupe.

        Args:
            k (int): Position de la liste
        """
        self.list_occupe[k] = 1
