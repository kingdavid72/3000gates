'''
Created on Aug 12, 2016

@author: Jae-Mun Choi and Mark Lee
This program requires Modeller v9.17 above.

'''

if __name__ == '__main__':
    pass

# Example for: model.read(), model.write()

# This will read a PDB file and write a CHARMM atom file without atomic charges
# or radii. For assigning charges and radii, see the all_hydrogen.py script.

from modeller import *
from modeller.scripts import complete_pdb, cispeptide

log.level(output=1, notes=1, warnings=1, errors=1, memory=0)
env = environ()
env.io.atom_files_directory = ['/home/storage/vina/ProteaseG2/HOV2_B1+ligand_53346/gromacs-ProteaseG2']

env.libs.topology.read(file='$(LIB)/top_heav.lib')
env.libs.parameters.read(file='$(LIB)/par.lib')

code = 'HOV2_B1.pdb'
mdl= complete_pdb(env, code, special_patches=None, transfer_res_num=True, 
                 model_segment=None, patch_default=True)



mdl.write(file='HOV2_B1-fixed.pdb')
#mdl.write(file='HOV2_B1.crd', model_format='CHARMM')
#mdl.write(file='HOV2_B1.cif', model_format='MMCIF')

'''
# This section is for adding Restraints such as cispeptides
rsr = mdl.restraints
atmsel = selection(mdl)
rsr.make(atmsel, restraint_type='stereo', spline_on_site=False)

# Change the Pro-56 restraint from trans to cis:
a = mdl.atoms
cispeptide(rsr, atom_ids1=(a['O:56'], a['C:56'], a['N:57'], a['CA:57']),
                    atom_ids2=(a['CA:56'], a['C:56'], a['N:57'], a['CA:57']))

# Constrain the distance between alpha carbons in residues 5 and 15 to
# be less than 10 angstroms:
rsr.add(forms.upper_bound(group=physical.xy_distance,
                              feature=features.distance(a['CA:5'], a['CA:15']),
                              mean=10., stdev=0.1))

rsr.write(file='1fas.rsr')
atmsel.energy()

'''
