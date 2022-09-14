"""Extracting, cleaning and creating the Atoms of the protein."""
import argparse
import Bio.PDB
import atome
import sys


def parse_argument():
    """Get the arguments of the commands in the terminal"""
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
    """Extract the 3 letters code of the residue.

    Args:
        residue (str): String extract by .get__parent() 

    Returns:
        str: 3 letters code
    """
    residue = residue.replace("<Residue", "")
    residue = residue[0:4]
    return residue.strip()


def mise_num(nom, chain):
    """Extract the number and the chain of the residue by atom.

    Args:
        nom (str): String extract by .get__parent() 

    Returns:
        str: Number of the residue and the chain
    """
    nom = nom.split("resseq=")[1]
    nom = nom.split("icode")[0]
    chain = chain.split("=")[1]
    chain = chain.split(">")[0]
    return nom+chain


def extract_proteine(atomes, data, nbr):
    """Create the objects atomes and add it to the list data.

    Args:
        atomes (generator): Generator that contains the structure of the protein
        data (list): Empty List
        nbr (int): Number of point by atome
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
    """Read the file pdb and extract the structure.

    Args:
        file (str): Name of the file
        data (list): Empty List 
        nbr (int): Number of point by atome
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
