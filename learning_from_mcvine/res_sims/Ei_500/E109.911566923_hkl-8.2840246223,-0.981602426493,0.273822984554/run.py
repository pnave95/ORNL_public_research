#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E109.911566923_hkl-8.2840246223,-0.981602426493,0.273822984554/sample/sampleassembly.xml'
psi = -0.0026369192021115494
hkl2Q = array([[ -6.58214469e-01,   9.36082306e-01,  -7.76551919e-17],
       [  6.61910147e-01,   4.65427914e-01,  -8.09165116e-01],
       [ -6.61910147e-01,  -4.65427914e-01,  -8.09165116e-01]])
pp = array([ 2.38958488,  1.81380377, -0.12457182])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017362297876039822
Q = array([ 4.62168605, -8.33883891,  0.57271043])
E = 109.91156692337518
hkl_projection = array([-0.09522423, -0.82799258, -0.88074836])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
