#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-19.328309895_hkl0.601280068587,-0.674061682188,0.337708393758/sample/sampleassembly.xml'
psi = -0.036339225175566134
hkl2Q = array([[ -6.26298529e-01,   9.57729881e-01,  -7.58999511e-17],
       [  6.77217293e-01,   4.42859937e-01,  -8.09165116e-01],
       [ -6.77217293e-01,  -4.42859937e-01,  -8.09165116e-01]])
pp = array([ 2.99897228, -0.07851924, -0.16722728])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.00666402257119365
Q = array([-1.06176901,  0.12779146,  0.27216535])
E = -19.328309894988585
hkl_projection = array([-0.76739127, -0.36974363,  0.81096754])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
