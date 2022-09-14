# Calculating the accessible surface area of a protein 
Calculate the accessible surface area (ASA) of a protein

# Set up

The program need a new environnement, that you can install with the file env.yml
```
conda env create -n name_of_your_env -f env.yml
```
To work the program need:
  - biopython=1.79
  - numpy=1.23.2
  - python=3.10.6
  - rich=12.5.1
  
  # Use
  In your terminal, write:
```
  python main.py -p nom_de_votre_fichier_pdb
```
  Others arguments may be use:
   - For the number of point by atom
    
    ```
        python main.py -p nom_de_votre_fichier_pdb -d 100
     ```
   - For the radius of the probe
    
    ```
        python main.py -p nom_de_votre_fichier_pdb -r 1.5
    ```
  - For the model to test. Only use this argument when your file was obtain by NMR 
    ```
        python main.py -p nom_de_votre_fichier_pdb -d 100 -m 1
    ```

# References
  - Radius of atoms:  A. Bondi, « Van der Waals Volumes and Radii », J. Phys. Chem., vol. 68, no 3,‎ 1964, p. 441–51 (DOI 10.1021/j100785a001, lire en ligne [archive])
  - Maximal accessible surface area : Tien, M. Z.; Meyer, A. G.; Sydykova, D. K.; Spielman, S. J.; Wilke, C. O. (2013). "Maximum allowed solvent accessibilites of residues in proteins". PLOS ONE. 8 (11): e80635. arXiv:1211.4251. Bibcode:2013PLoSO...880635T. doi:10.1371/journal.pone.0080635. PMC 3836772. PMID 24278298.
  - Saff, E.B., Kuijlaars, A.B.J. Distributing many points on a sphere. The Mathematical Intelligencer 19, 5–11 (1997). https://doi.org/10.1007/BF03024331 
  -Shrake, A; Rupley, JA. (1973). "Environment and exposure to solvent of protein atoms. Lysozyme and insulin". J Mol Biol 79 (2): 351–71. doi:10.1016/0022-2836(73)90011-9.
  
