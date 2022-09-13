"""Calcul des coordonnées sphérique et x,y,z des points."""
import math


def securite_radius(angle):
    """
    Retourne -0.9999, 0.9999 ou angle afin d'éviter de diviser par 0.

    Args:
        angle (float): Angle
    Returns:
        angle: Angle
    """
    if angle < -1:
        return float(-0.9999)
    if angle > 1:
        return float(0.9999)
    return angle


def algo_saff(nbr):
    """Retourne les coordonnées sphérique de tous les points d'une sphére.

    Args:
        nbr (int): Nombre de point par atome

    Returns:
        theta (float): Liste des coordonées theta
        phi (float): Liste des coordonées theta
    """
    theta = []
    phi = []
    for entier in range(nbr):
        angle = - 1 + (2 * (entier - 1) / (nbr - 1))
        theta.append(math.acos(securite_radius(angle)))
        if entier == 0 or entier == nbr:
            phi.append(0)
        else:
            result = ((phi[entier-1] + (3.6 / math.sqrt(nbr) * (1 / math.sqrt(
                        1 - ((angle ** 2) - 0.00000001))))) % (2 * math.pi))
            phi.append(result)
    return theta, phi


def calcul_points(theta, phi, position, rayon, nbr, probe):
    """Retourne une liste de coordonnées (x,y,z) de points d'un atome.

    Args:
        theta (float): Coordonées theta
        phi (float): Coordonées phi
        position (array): Coordonnées du centre de l'atome
        rayon (float): Rayon de l'atome
        nbr (int): Nombre de point sur l'atome
        probe (float): Rayon de la sonde

    Returns:
        list: Liste contenant les coordonées des points d'un atome
    """
    data = []
    for entier in range(nbr):
        point = []
        point.append(((rayon + probe)*math.sin(theta[entier]) *
                      math.cos(phi[entier])) + position[0])
        point.append(((rayon + probe)*math.sin(theta[entier]) *
                      math.sin(phi[entier])) + position[1])
        point.append(((rayon + probe) * math.cos(theta[entier])) + position[2])
        data.append(point)
    return data


def create_point(data, nbr, probe):
    """Ajoute les coordonnées des points pour chaque atome.

    Args:
        data (liste): Liste des atomes
        nbr (int): Nombre de point sur l'atome
        probe (float): Rayon de la sonde
    """
    coord_sphere = algo_saff(nbr)
    for atom in data:
        atom.set_list_position(calcul_points(coord_sphere[0], coord_sphere[1],
                                             atom.coordone, atom.rayon, nbr,
                                             probe))
