import numpy as np

def open_pdb(file_location):
    """
    Reads in a pdb file and returns the atom names and coordinates.

    The pdb file must specify the atom elements in the last column, and follow the conventions outlines in the PDB format specification.

    Parameters
    ----------
    file_location: str
        The location of the pdb file.

    Returns
    -------
    symbols : list
        The atom symbols of the pdb file.
    coords : np.ndarray
        The atomic coordinates.

    """

    with open(file_location) as f:
        data = f.readlines()

    coordinates = []
    symbols = []

    for line in data:
        if 'ATOM' in line[0:6] or 'HETATM' in line[0:6]:
            symbols.append(line[76:79].strip())
            c2 = [float(x) for x in line[30:55].split()]
            coordinates.append(c2)

    coords = np.array(coordinates)

    return symbols, coords
