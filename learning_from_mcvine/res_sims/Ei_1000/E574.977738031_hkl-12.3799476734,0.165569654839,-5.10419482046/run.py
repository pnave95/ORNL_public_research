#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E574.977738031_hkl-12.3799476734,0.165569654839,-5.10419482046/sample/sampleassembly.xml'
psi = -0.006921177406214792
hkl2Q = array([[ -6.54198022e-01,   9.38893668e-01,  -7.74226663e-17],
       [  6.63898079e-01,   4.62587858e-01,  -8.09165116e-01],
       [ -6.63898079e-01,  -4.62587858e-01,  -8.09165116e-01]])
pp = array([ 2.25702986,  1.97631379, -0.85977668])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.001324670041172303
Q = array([ 11.59752379,  -9.18572542,   3.99616321])
E = 574.97773803064297
hkl_projection = array([-0.95825241,  0.21534105,  0.99164167])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
