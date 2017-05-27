#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E17.5453841191_hkl-2.9803137886,0.919747624624,1.53363111804/sample/sampleassembly.xml'
psi = -0.0024479689361019074
hkl2Q = array([[ -6.58391330e-01,   9.35957920e-01,  -7.76655121e-17],
       [  6.61822192e-01,   4.65552974e-01,  -8.09165116e-01],
       [ -6.61822192e-01,  -4.65552974e-01,  -8.09165116e-01]])
pp = array([ 2.69167416,  1.32472268,  0.85515965])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0034679317348414009
Q = array([ 1.55593104, -3.07524358, -1.9851885 ])
E = 17.545384119053466
hkl_projection = array([-0.97618112, -0.29730163, -0.15953588])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
