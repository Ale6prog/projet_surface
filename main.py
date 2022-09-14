"""Script permettant de calculer la surface accésible d'une protéine.

Usage:
======
    python main.py -p name -d points -r sonde

    name: a file .pdb
    points: Number of point by atome(par défaut 92)
    sonde : Radius of the probe (par défaut 1.4 A)
    model : Number of the model (for NMR only)

"""

__authors__ = ("Alexis Bel")
__contact__ = ("alexbel28@yahoo.fr")
__date__ = "2022-09-11"
__version__ = "1.0"
import input
import sphere
import calcul


def main(pdb, nbr, probe, model):
    """Main Function.

    Args:
        pdb (str): Name of the file pdb
        nbr (int): Number of point by atome
        probe (float): Radius of the probe 
    """
    data = []
    input.extract_data(pdb, data, nbr, model)
    sphere.create_point(data, nbr, probe)
    calcul.shrake_rupley(data, nbr, probe)
    calcul.accesible_surface(data)


if __name__ == '__main__':
    # Get the arguments 
    result_args = input.parse_argument()
    # Run main
    main(result_args.pdb[0], result_args.nbr, result_args.probe,
         result_args.modele)
