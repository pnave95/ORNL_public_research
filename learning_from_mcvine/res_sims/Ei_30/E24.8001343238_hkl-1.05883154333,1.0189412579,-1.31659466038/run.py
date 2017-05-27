#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E24.8001343238_hkl-1.05883154333,1.0189412579,-1.31659466038/sample/sampleassembly.xml'
psi = 0.05187710190620203
hkl2Q = array([[ -7.08241017e-01,   8.98827588e-01,   8.08738540e-17],
       [  6.35567083e-01,   5.00802026e-01,  -8.09165116e-01],
       [ -6.35567083e-01,  -5.00802026e-01,  -8.09165116e-01]])
pp = array([ 2.97203089, -0.40869594, -0.45167193])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0086666311675906681
Q = array([ 2.23429768,  0.21793412,  0.24085075])
E = 24.800134323757682
hkl_projection = array([ 0.07173856, -0.10317488, -0.0077245 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
