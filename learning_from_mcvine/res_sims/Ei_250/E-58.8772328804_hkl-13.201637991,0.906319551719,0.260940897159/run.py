#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-58.8772328804_hkl-13.201637991,0.906319551719,0.260940897159/sample/sampleassembly.xml'
psi = -0.002712536685234317
hkl2Q = array([[ -6.58143683e-01,   9.36132076e-01,  -7.76510633e-17],
       [  6.61945339e-01,   4.65377861e-01,  -8.09165116e-01],
       [ -6.61945339e-01,  -4.65377861e-01,  -8.09165116e-01]])
pp = array([ 0.46878008,  2.96314786,  0.23210164])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023581593224142397
Q = array([  9.11578004, -12.05813184,  -0.94450644])
E = -58.877232880356587
hkl_projection = array([ 0.29051255, -0.70413657, -0.05689334])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
