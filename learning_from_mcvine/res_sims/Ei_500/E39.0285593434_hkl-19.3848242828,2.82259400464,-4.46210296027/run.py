#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E39.0285593434_hkl-19.3848242828,2.82259400464,-4.46210296027/sample/sampleassembly.xml'
psi = -0.005649195559300667
hkl2Q = array([[ -6.55391748e-01,   9.38060780e-01,  -7.74914085e-17],
       [  6.63309139e-01,   4.63431950e-01,  -8.09165116e-01],
       [ -6.63309139e-01,  -4.63431950e-01,  -8.09165116e-01]])
pp = array([-0.3875274 ,  2.97486512, -0.26651182])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017098339265254078
Q = array([ 17.53665995, -14.80818208,   1.32663346])
E = 39.028559343391748
hkl_projection = array([-0.18487075, -0.94772595,  0.72704319])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
