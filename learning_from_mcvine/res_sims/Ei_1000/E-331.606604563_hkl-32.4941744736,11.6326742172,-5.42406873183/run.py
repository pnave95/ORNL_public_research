#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-331.606604563_hkl-32.4941744736,11.6326742172,-5.42406873183/sample/sampleassembly.xml'
psi = -0.007890609245511559
hkl2Q = array([[ -6.53287521e-01,   9.39527427e-01,   7.73704407e-17],
       [  6.64346215e-01,   4.61944036e-01,  -8.09165116e-01],
       [ -6.64346215e-01,  -4.61944036e-01,  -8.09165116e-01]])
pp = array([-1.25894104,  2.72306215,  0.60397969])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011739024708065197
Q = array([ 32.55962131, -22.64990744,  -5.02378698])
E = -331.60660456339451
hkl_projection = array([ 0.46757493,  0.17289388,  0.98286258])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
