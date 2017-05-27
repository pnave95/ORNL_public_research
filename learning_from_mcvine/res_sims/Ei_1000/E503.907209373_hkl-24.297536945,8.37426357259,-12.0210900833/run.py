#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E503.907209373_hkl-24.297536945,8.37426357259,-12.0210900833/sample/sampleassembly.xml'
psi = -0.012005329584558848
hkl2Q = array([[-0.64941611,  0.94220756,  0.        ],
       [ 0.66624136,  0.45920653, -0.80916512],
       [-0.66624136, -0.45920653, -0.80916512]])
pp = array([-1.4215928 ,  2.64179369, -0.57627398])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012931241171901114
Q = array([ 29.36743998, -13.52764335,   2.9508848 ])
E = 503.90720937273272
hkl_projection = array([-0.05430263, -0.24033361,  0.12843319])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
