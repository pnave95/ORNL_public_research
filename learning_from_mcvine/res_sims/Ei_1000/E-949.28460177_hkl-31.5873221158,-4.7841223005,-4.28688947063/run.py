#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-949.28460177_hkl-31.5873221158,-4.7841223005,-4.28688947063/sample/sampleassembly.xml'
psi = -0.0037435917584368655
hkl2Q = array([[ -6.57178129e-01,   9.36810161e-01,   7.75948577e-17],
       [  6.62424817e-01,   4.64695112e-01,  -8.09165116e-01],
       [ -6.62424817e-01,  -4.64695112e-01,  -8.09165116e-01]])
pp = array([ 0.1666178 ,  2.99536951, -0.73722644])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.001142480940478107
Q = array([ 20.42911789, -29.82238598,   7.3399463 ])
E = -949.28460176992348
hkl_projection = array([-0.60475538, -0.31477892,  0.15239073])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
