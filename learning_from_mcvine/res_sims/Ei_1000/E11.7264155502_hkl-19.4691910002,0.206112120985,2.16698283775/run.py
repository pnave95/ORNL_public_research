#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E11.7264155502_hkl-19.4691910002,0.206112120985,2.16698283775/sample/sampleassembly.xml'
psi = -0.0032830133757219735
hkl2Q = array([[ -6.57609534e-01,   9.36507380e-01,  -7.76199448e-17],
       [  6.62210719e-01,   4.65000161e-01,  -8.09165116e-01],
       [ -6.62210719e-01,  -4.65000161e-01,  -8.09165116e-01]])
pp = array([ 1.45140807,  2.6255313 ,  0.26334046])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012007700021017507
Q = array([ 11.50461602, -19.14484624,  -1.92022566])
E = 11.726415550210618
hkl_projection = array([ 0.75369434, -0.1179844 ,  0.08468846])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
