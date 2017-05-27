#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E4.62673373838_hkl-4.36425819525,-0.331237778015,0.184695497196/sample/sampleassembly.xml'
psi = -0.0027983725117012403
hkl2Q = array([[ -6.58063327e-01,   9.36188565e-01,  -7.76463779e-17],
       [  6.61985283e-01,   4.65321041e-01,  -8.09165116e-01],
       [ -6.61985283e-01,  -4.65321041e-01,  -8.09165116e-01]])
pp = array([ 1.66108875,  2.49815615, -0.06847766])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0049380850565987119
Q = array([ 2.53041803, -4.32584323,  0.1185769 ])
E = 4.6267337383819935
hkl_projection = array([-0.13994844, -0.07583566,  0.3407105 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
