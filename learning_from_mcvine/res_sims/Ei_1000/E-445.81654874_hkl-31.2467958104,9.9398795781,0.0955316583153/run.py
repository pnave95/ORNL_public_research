#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-445.81654874_hkl-31.2467958104,9.9398795781,0.0955316583153/sample/sampleassembly.xml'
psi = -0.005971780904244944
hkl2Q = array([[ -6.55089110e-01,   9.38272151e-01,  -7.74739515e-17],
       [  6.63458601e-01,   4.63217952e-01,  -8.09165116e-01],
       [ -6.63458601e-01,  -4.63217952e-01,  -8.09165116e-01]])
pp = array([-0.58391089,  2.94262605,  0.96514653])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011717296807453579
Q = array([ 27.00075294, -24.75791965,  -8.1203047 ])
E = -445.81654874047803
hkl_projection = array([-0.11458493, -0.29379095, -0.87263772])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
