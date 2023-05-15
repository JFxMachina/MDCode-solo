#!/usr/bin/env python3
"""An example that demonstrates molecular dynamics with constant energy."""

# from asap3 import Trajectory
# from asap3 import EMT

from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase import units
from ase.atoms import Atoms
from ase.io import Trajectory

# For OpenKim models/potentials
from ase.calculators.kim.kim import KIM

# For loading MP materials
from mdcode.db.mp import load_materials
from pymatgen.io.ase import AseAtomsAdaptor

size = 10

def setup_atoms():
    summary, materials = load_materials(["Ti"], (1,1), cache_key="Ti")
    atoms = AseAtomsAdaptor.get_atoms(materials.structure[6])
    return atoms*(10,10,10)

def calcenergy(atoms):
    """Calculate the potential, kinetic and total energy per atom."""
    epot = atoms.get_potential_energy() / len(atoms)
    ekin = atoms.get_kinetic_energy() / len(atoms)
    Tinst = ekin / (1.5 * units.kB)
    etot = epot + ekin
    return (epot, ekin, Tinst, etot)

def run_md(atoms, output_filename="out.traj"):
    """Run an example MD simulation for a Cu fcc crystal."""

    # Universal
    # atoms.calc = KIM('LJ_ElliottAkerson_2015_Universal__MO_959249795837_003')

    # Titanium
    # atoms.calc = KIM('EAM_Dynamo_ZhouJohnsonWadley_2004NISTretabulation_Ti__MO_101966451181_000')

    # Titanium-Nitride
    # atoms.calc = KIM('MEAM_LAMMPS_AlmyrasSangiovanniSarakinos_2019_NAlTi__MO_958395190627_002')
    # atoms.calc = KIM('MEAM_LAMMPS_KimLee_2008_TiN__MO_070542625990_002')
    # atoms.calc = KIM('MEAM_LAMMPS_MirazDhariwalMeng_2020_CuNTi__MO_122936827583_002')

    # Set the momenta corresponding to T=300K
    MaxwellBoltzmannDistribution(atoms, temperature_K=300)

    # We want to run MD with constant energy using the VelocityVerlet algorithm.
    dyn = VelocityVerlet(atoms, 5*units.fs)  # 5 fs time step.
    traj = Trajectory(output_filename, "w", atoms)
    dyn.attach(traj.write, interval=5)

    def printenergy(a=atoms):  # store a reference to atoms in the definition.
        """Print the potential, kinetic and total energy per atom."""
        res = calcenergy(a)
        print('Energy per atom: Epot = %.3feV  Ekin = %.3feV (T=%3.0fK)  '
              'Etot = %.3feV' % res)

    # Now run the dynamics
    dyn.attach(printenergy, interval=10)
    printenergy()
    dyn.run(200)


if __name__ == "__main__":
    atoms = setup_atoms()
    run_md(atoms)
