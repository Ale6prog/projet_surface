# Calcul de la surface accésible d'une protéine
Permet de calculer la surface accéssible d'une protéine

# Installation

Afin de faire fonctionner le programme, installer un nouvel environnement avec le fichier yml.
Pour fonctionner, le programme a besoin de:
  - biopython=1.79
  - numpy=1.23.2
  - python=3.10.6
  - rich=12.5.1
  
  # Usage
  
  Dans votre terminal, écrivez:
  ```
  python main.py -p nom_de_votre_fichier_pdb
  ```
  D'autre arguments peuvent étre donner pour plus de personnalisation telle que:
   - Pour le nombre de points par atome
    
    ```
        python main.py -p nom_de_votre_fichier_pdb -d 100
     ```
   - Pour le rayon de la sonde
    
    ```
        python main.py -p nom_de_votre_fichier_pdb -r 1.5
    ```
  - Pour le modèle à tester. Cet argument ne sert qu'au fichier pdb obtenue par NMR.
    ```
        python main.py -p nom_de_votre_fichier_pdb -d 100 -m 1
    ```

# References
  - Rayon des atomes :  A. Bondi, « Van der Waals Volumes and Radii », J. Phys. Chem., vol. 68, no 3,‎ 1964, p. 441–51 (DOI 10.1021/j100785a001, lire en ligne [archive])
  - Surface accéssible maximale : Tien, M. Z.; Meyer, A. G.; Sydykova, D. K.; Spielman, S. J.; Wilke, C. O. (2013). "Maximum allowed solvent accessibilites of residues in proteins". PLOS ONE. 8 (11): e80635. arXiv:1211.4251. Bibcode:2013PLoSO...880635T. doi:10.1371/journal.pone.0080635. PMC 3836772. PMID 24278298.
  - Saff, E.B., Kuijlaars, A.B.J. Distributing many points on a sphere. The Mathematical Intelligencer 19, 5–11 (1997). https://doi.org/10.1007/BF03024331 
  -Shrake, A; Rupley, JA. (1973). "Environment and exposure to solvent of protein atoms. Lysozyme and insulin". J Mol Biol 79 (2): 351–71. doi:10.1016/0022-2836(73)90011-9.
  
