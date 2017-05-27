#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-3.5884933114_hkl-2.16654799123,-0.222680741809,1.44644382654/sample/sampleassembly.xml'
psi = -0.0004185819529624998
hkl2Q = array([[ -6.60289394e-01,   9.34619863e-01,  -7.77767026e-17],
       [  6.60876043e-01,   4.66895108e-01,  -8.09165116e-01],
       [ -6.60876043e-01,  -4.66895108e-01,  -8.09165116e-01]])
pp = array([ 2.90192482,  0.76081032,  0.26865885])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023987741497479491
Q = array([ 0.32746422, -2.80420488, -0.9902264 ])
E = -3.5884933114035391
hkl_projection = array([-0.94469412, -0.7339053 , -0.19889375])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
