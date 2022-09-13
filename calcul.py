"""Calcul de l'enfouissement de chaque point des atomes."""
import math
import rich.table
import rich.progress


def shrake_rupley(data, nbr, probe):
    """Algorithme de shrake_rupley.

    Args:
        data (List): Liste des atomes
        nbr (int): Nombre des points sur un atome
        probe (float): Rayon de la sond
    """
    print("||Calculating accessible surface of each atoms||")
    for atom in rich.progress.track(data, description='[green]Calculating'):
        iterateur = detect_voisin(data, atom)
        for i in iterateur:
            for k in range(nbr):
                if atom.list_occupe[k] is not True:
                    if(math.dist(atom.list_position[k], data[i].coordone) <
                            data[i].rayon + probe):
                        atom.set_occupe(k)
        atom.set_surface()


def detect_voisin(data, centre):
    """Retourne une liste contenant le numéro des atomes voisins.

    Args:
        data (List): Liste des atomes
        centre (array): Array des coordonnées de points

    Returns:
        list: Liste des numéros des atomes voisins
    """
    return [i for i in range(len(data)) if math.dist(centre.coordone,
            data[i].coordone)]


def surface_residue(data):
    """Retourne un dictionnaire contenant la surface de chaque résidus.

    Args:
        data (list): Liste des atomes

    Returns:
        dictionnaire: Contient les clés (residues, chain and number of
        residues) et objets (surface)
    """
    memoire = {}
    for atom in data:
        name = atom.num + " " + atom.residu
        if name not in memoire.keys():
            memoire[name] = atom.surface
        else:
            memoire[name] += atom.surface
    return memoire


def accesible_surface(data):
    """Compose la table des résultats.

    Args:
        data (List): Liste des atomes
    """
    print("||Calculating relative surface for each residu||")
    table = rich.table.Table(title="Results")
    acide = {"ALA": 121, "ARG": 265, "ASN": 187, "ASP": 187, "CYS": 148,
             "GLU": 214, "GLN": 214, "GLY": 97, "HIS": 216, "ILE": 195,
             "LEU": 191, "LYS": 230, "MET": 203, "PHE": 228, "PRO": 154,
             "SER": 143, "THR": 163, "TRP": 264, "TYR": 255, "VAL": 165}
    phobe = ["ALA", "ILE", "LEU", "MET", "PHE", "TRP", "TYR", "VAL",
             "GLY", "PRO"]
    phile = ["ASP", "GLU", "ARG", "ASN", "GLN", "HIS", "LYS", "SER",
             "THR", "CYS"]
    memoi = surface_residue(data)
    table.add_column("Residue", style="cyan", no_wrap=True)
    table.add_column("ASA (Angstrom**2)", justify="center", style="magenta")
    table.add_column("RASA", justify="center", style="green")
    hydrophobe = 0
    hydrophile = 0
    partie = 0
    total = 0
    for residu in memoi:
        if residu[-3:] in acide:
            if residu[-3:] in phile:
                hydrophile += memoi[residu]
            if residu[-3:] in phobe:
                hydrophobe += memoi[residu]
            partie += memoi[residu]
            total += acide[residu.split()[2]]
            table.add_row(residu, str(round(memoi[residu], 0)),
                          str(round(memoi[residu]/acide[residu.split()[2]],
                                    3)))
        else:
            table.add_row(residu, str(round(memoi[residu], 2)),
                          str("Non calculable"))
    good_print(table, partie, total, hydrophile, hydrophobe)


def good_print(table, partie, total, phile, phobe):
    """Affiche les résultats.

    Args:
        table (table): Un tableau contenant les surfaces des résidus
        partie (float): La surface accésible calculé
        total (float): La surface maximum accessible de la protéine
    """
    rich.print(table)
    rich.print(f"\n Surface accessible des acides aminées hydrophobe : \
                 {round(phobe,3)} angstrom**2")
    rich.print(f"\n Surface accessible des acides aminées hydrophile : \
                {round(phile,3)} angstrom**2")
    rich.print(f"\n Surface accessible total : {round(partie,0)} angstrom**2")
    rich.print(f"\n {round(partie/total*100, 0)} % of the protein is exposed "
               "to the solvant\n")
