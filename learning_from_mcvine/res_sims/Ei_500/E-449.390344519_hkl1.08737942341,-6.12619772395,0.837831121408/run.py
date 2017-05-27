#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-449.390344519_hkl1.08737942341,-6.12619772395,0.837831121408/sample/sampleassembly.xml'
psi = 0.011103393714127809
hkl2Q = array([[-0.67101399,  0.92695016,  0.        ],
       [ 0.65545274,  0.47447855, -0.80916512],
       [-0.65545274, -0.47447855, -0.80916512]])
pp = array([ 2.98205756,  0.32761675, -0.61050528])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.001617359407341773
Q = array([-5.2942386 , -2.29633576,  4.27916178])
E = -449.39034451859737
hkl_projection = array([ 0.42872609,  0.85775094, -0.9099347 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
