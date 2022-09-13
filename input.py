"""Extraction, mise en forme et création des Atom de la protéine."""
import argparse
import Bio.PDB
import atome
import sys


def parse_argument():
    """Permet de récupérer les arguments de la commande dans le terminal."""
    parser = argparse.ArgumentParser(description="Calcul de la surface \
                                            accessible d'une protéine")
    parser.add_argument("-p", dest="pdb", help="Nom du fichier pdb", nargs=1)
    parser.add_argument("-d", dest="nbr", help="Nombre de points par atome. \
                        Par défaut 92 points", nargs="?", default=92, type=int)
    parser.add_argument("-r", dest="probe", help="Rayon de la sonde. Par \
                        défaut 1.4 A",
                        nargs="?", default=1.4, type=int)
    parser.add_argument("-m", dest="modele", help="Numéro du modèle à tester. \
                        Par défaut n°1. A utiliser pour les structures \
                        obtenues par RMN",
                        nargs="?", default=0, type=int)
    return parser.parse_args()


def mise_res(residue):
    """Extrait le code à 3 lettres du résidue.

    Args:
        residue (str): String extrait par .get__parent() de PDB

    Returns:
        str: Code à 3 lettres du résidues
    """
    residue = residue.replace("<Residue", "")
    residue = residue[0:4]
    return residue.strip()


def mise_num(nom, chain):
    """Extrait le numéro du résidu par atom.

    Args:
        nom (str): String extrait par .get__parent() de PDB

    Returns:
        str: Numéro du résidu
    """
    nom = nom.split("resseq=")[1]
    nom = nom.split("icode")[0]
    chain = chain.split("=")[1]
    chain = chain.split(">")[0]
    return nom+chain


def extract_proteine(atomes, data, nbr):
    """Création des objets atomes et ajout des objets à la list data.

    Args:
        atomes (generator): Generator contenant la structure de la protéine
        data (list): List vide
        nbr (int): Nombre de point par atome
    """
    acide = ["ALA", "ARG", "ASN", "ASP", "CYS", "GLU", "GLN", "GLY",
             "HIS", "ILE", "LEU", "LYS", "MET", "PHE", "PRO", "SER",
             "THR", "TRP", "TYR", "VAL"]
    for particule in atomes:
        residue = particule.get_parent()
        residue_str = mise_res(str(residue))
        if residue_str not in acide:
            continue
        point = atome.Atome(mise_num(str(residue), str(residue.get_parent())),
                            residue_str, particule.get_coord(),
                            particule.element, nbr)
        data.append(point)


def extract_data(file, data, nbr, model):
    """Lecture du fichier pdb et extraction de la structure.

    Args:
        file (str): Nom du fichier pdb
        data (list): List vide
        nbr (int): Nombre de point par atome
    """
    try:
        parser = Bio.PDB .PDBParser()
        id = file.split(".")[0]
        structure = parser.get_structure(id, file)
        print(f"> File {file} found")
        if structure.header["structure_method"] == "x-ray diffraction":
            atomes = structure.get_atoms()
            extract_proteine(atomes, data, nbr)
        elif structure.header["structure_method"] == "solution nmr":
            print(f"Attention contient plusieurs modèles. \
                    Sélection du modèle n°{model}")
            atomes = structure[model].get_atoms()
            extract_proteine(atomes, data, nbr)
    except FileNotFoundError:
        print(f"File not found")
        sys.exit()
