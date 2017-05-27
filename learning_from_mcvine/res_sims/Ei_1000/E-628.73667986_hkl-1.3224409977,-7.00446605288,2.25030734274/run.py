#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-628.73667986_hkl-1.3224409977,-7.00446605288,2.25030734274/sample/sampleassembly.xml'
psi = 0.005105035348378203
hkl2Q = array([[ -6.65441777e-01,   9.30958438e-01,  -7.80825955e-17],
       [  6.58287024e-01,   4.70538393e-01,  -8.09165116e-01],
       [ -6.58287024e-01,  -4.70538393e-01,  -8.09165116e-01]])
pp = array([ 2.93910854,  0.60136596, -0.41415158])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011539453444802973
Q = array([-5.21228975, -5.58586381,  3.84689939])
E = -628.73667985984093
hkl_projection = array([ 0.47383966, -0.79146617, -0.97395054])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
