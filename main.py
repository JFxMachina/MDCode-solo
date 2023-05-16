from os import remove
from datetime import datetime

from mdcode.material.mp import load_materials, get_atoms, get_elements
from mdcode.material.atoms import scale
from mdcode.potential.kim import get_potentials
from mdcode.calc.md import run_md
from mdcode.calc.analyse import analyse, visualise

def run_all(materials):
    for potential in potentials:
        for material in materials.iterrows():
            atoms = scale(get_atoms(material))
            run_id = material.material_id + potential.split('__')[1] + \
                datetime.now().replace(microsecond=0).isoformat().replace(':','')
            output_filename = run_id + ".traj"
            run_md(atoms, potential, output_filename)
            analyse(material, potential, output_filename)
            remove(output_filename)
    visualise(materials)


if __name__ == '__main__':
    summary, materials = load_materials(["Ti"], (1,1), cache_key="Ti")
    potentials = get_potentials(get_elements(materials))
    run_all(materials, potentials)

    summary, materials = load_materials(["Ti","N"], (2,2), cache_key="TiN")
    potentials = get_potentials(get_elements(materials))
    run_all(materials, potentials)
