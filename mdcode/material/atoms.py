#!/usr/bin/env python3
"""Prepare atoms for simulation."""

import numpy as np

from math import pow, ceil
from ase.atoms import Atoms

def scale(atoms, target_natoms=1000) -> Atoms:
    """
    Repeat the cell to create a supercell containing at least <target_natoms>
    atoms.

    Parameters
    ----------
    atoms : ase.atoms.Atoms
        A collection of atoms.
    target_natoms : positive integer, optional
        DESCRIPTION. The default is 1000.

    Returns
    -------
    ase.atoms.Atoms
        Supercell of atoms.

    """
    natoms = len(atoms)
    ratio = pow(target_natoms/natoms, 1/3)
    ls = atoms.cell.lengths()
    #ls[:] = 1 # FIXME
    l = pow(ls.prod(), 1/3)
    rs = np.zeros_like(ls, dtype=int)
    rcum = ratio
    for i in np.flip(ls.argsort()):
        rs[i] = ceil(rcum)
        rcum *= ratio/rs[i]
    return atoms*tuple(rs)
