"""Objects representing an atom."""
import numpy as np
RAYON = {"H": 1.20, "C": 1.70, "N": 1.55, "O": 1.4, "F": 1.47,
         "NA": 2.27, "MG": 1.73, "SI": 2.1, "P": 1.8, "S": 1.8,
         "CL": 1.75, "K": 2.75, "CU": 1.4, "ZN": 1.39, "SE": 1.9,
         "BR": 1.85, "I": 1.98, "MN": 2.05, "AL": 1.84, "FE": 1.94,
         "CA": 2.31, "AG": 2.03}


class Atome:
    """An atom."""

    def __init__(self, numero, residu, coordone, element, nbr):
        """Objects representing an atom and his properties.

        Args:
            num (str): Number and chain of the residue
            residu (str): 3 letter code
            coordone (array): Coordinates of the center
            element (str): Element of the atom
            nbr (int): Number of point by atome
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
        """Set the radius by his element."""
        if self.element in RAYON:
            self.rayon = RAYON[self.element]

    def set_list_position(self, pos):
        """Set le array of positions of each points.

        Args:
            pos (list): list of positions of the points
        """
        self.list_position = np.array(pos)

    def set_surface(self):
        """Set the surface."""
        self.surface = (((4 * np.pi) / (len(self.list_occupe))) *
                        ((self.rayon+1.4)**2)) * self.compte_libre()

    def compte_libre(self):
        """Count the number of free points..

        Returns:
            int: Number of free points
        """
        return len(self.list_occupe)-(sum(self.list_occupe))

    def compte_pris(self):
        """Count the number of buried points.

        Returns:
            int: Number of buried points
        """
        return (len(self.list_occupe)) - self.compte_libre(self)

    def set_occupe(self, k):
        """Set a position in the list as buried.

        Args:
            k (int): Position in the list
        """
        self.list_occupe[k] = 1
