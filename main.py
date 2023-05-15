from mdcode.db.mp import load_materials
from mdcode.calc.md import setup_atoms, run_md

atoms = setup_atoms()
run_md(atoms)