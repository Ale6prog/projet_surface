"""Calculate the spherical coordinates of points."""
import math


def securite_radius(angle):
    """
    Return -0.9999, 0.9999 or angle to avoid the division 0.

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
    """Return the spherical coordinates of all points of a sphere.

    Args:
        nbr (int): Number of point by atome

    Returns:
        theta (float):  List of the coordinate  theta
        phi (float): List of the coordinate phi 
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
    """Reture a list of coordinate (x,y,z) of points of a atom.

    Args:
        theta (float): Coordinate theta
        phi (float): Coordinate phi
        position (array): Coordinate of the centre of the atom
        rayon (float): Radius of the atome
        nbr (int): Number of point by atome
        probe (float): Radius of a the probe

    Returns:
        list: List of the coordinates of all points of a atom
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
    """Add the coordinates of points for all the atoms.

    Args:
        data (liste): List of atoms
        nbr (int): Number of point by atome
        probe (float): Radius of a the probe
    """
    coord_sphere = algo_saff(nbr)
    for atom in data:
        atom.set_list_position(calcul_points(coord_sphere[0], coord_sphere[1],
                                             atom.coordone, atom.rayon, nbr,
                                             probe))
