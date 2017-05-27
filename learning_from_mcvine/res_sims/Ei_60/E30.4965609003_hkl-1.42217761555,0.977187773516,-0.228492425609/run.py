#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E30.4965609003_hkl-1.42217761555,0.977187773516,-0.228492425609/sample/sampleassembly.xml'
psi = -0.010660330881827277
hkl2Q = array([[ -6.50682790e-01,   9.41333245e-01,  -7.72220162e-17],
       [  6.65623121e-01,   4.60102213e-01,  -8.09165116e-01],
       [ -6.65623121e-01,  -4.60102213e-01,  -8.09165116e-01]])
pp = array([ 2.93411161,  0.62529119,  0.48317526])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0052876003622715599
Q = array([ 1.72791512, -0.78400694, -0.60581816])
E = 30.49656090033929
hkl_projection = array([ 0.0776879 ,  0.95562841,  0.46246384])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
