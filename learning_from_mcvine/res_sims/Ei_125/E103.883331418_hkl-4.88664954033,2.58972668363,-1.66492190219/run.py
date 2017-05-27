#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E103.883331418_hkl-4.88664954033,2.58972668363,-1.66492190219/sample/sampleassembly.xml'
psi = -0.011127708375349477
hkl2Q = array([[-0.65024276,  0.94163726,  0.        ],
       [ 0.66583809,  0.45979107, -0.80916512],
       [-0.66583809, -0.45979107, -0.80916512]])
pp = array([ 1.68390984,  2.48283058,  0.70238541])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0042745217209808973
Q = array([ 6.01041557, -2.64520186, -0.74831977])
E = 103.88333141759455
hkl_projection = array([ 0.97980017, -0.51305986,  0.2084836 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
