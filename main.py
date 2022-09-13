"""Script permettant de calculer la surface accésible d'une protéine.

Usage:
======
    python main.py -p name -d points -r sonde

    name: un fichier pdb
    points: Nombre de points par atome (par défaut 92)
    sonde : rayon de la sonde (par défaut 1.4 A)

"""

__authors__ = ("Alexis Bel")
__contact__ = ("alexbel28@yahoo.fr")
__date__ = "2022-09-11"
__version__ = "1.0"
import input
import sphere
import calcul


def main(pdb, nbr, probe, model):
    """Fonction principale.

    Args:
        pdb (str): Nom du fichier pdb
        nbr (int): Nombre de point par atome
        probe (float): Rayon de la sonde utilisé
    """
    data = []
    input.extract_data(pdb, data, nbr, model)
    sphere.create_point(data, nbr, probe)
    calcul.shrake_rupley(data, nbr, probe)
    calcul.accesible_surface(data)


if __name__ == '__main__':
    # récupére les arguments de la fonction
    result_args = input.parse_argument()
    # lance la fonction principale
    main(result_args.pdb[0], result_args.nbr, result_args.probe,
         result_args.modele)
