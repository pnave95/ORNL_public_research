#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E219.779786874_hkl-7.86567446977,4.41166950723,-3.43000188238/sample/sampleassembly.xml'
psi = -0.009917586150227918
hkl2Q = array([[ -6.51381780e-01,   9.40849695e-01,  -7.72617045e-17],
       [  6.65281199e-01,   4.60596474e-01,  -8.09165116e-01],
       [ -6.65281199e-01,  -4.60596474e-01,  -8.09165116e-01]])
pp = array([ 0.53221469,  2.95241385,  0.61901817])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032055826648198834
Q = array([ 10.34047358,  -3.78857123,  -0.7943312 ])
E = 219.77978687414731
hkl_projection = array([ 0.35463578,  0.22995691,  0.14810003])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
