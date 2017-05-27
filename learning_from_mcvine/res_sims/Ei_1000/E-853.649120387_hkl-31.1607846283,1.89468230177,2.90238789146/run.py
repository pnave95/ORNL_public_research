#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-853.649120387_hkl-31.1607846283,1.89468230177,2.90238789146/sample/sampleassembly.xml'
psi = -0.003650638227660531
hkl2Q = array([[ -6.57265206e-01,   9.36749070e-01,  -7.75999181e-17],
       [  6.62381620e-01,   4.64756684e-01,  -8.09165116e-01],
       [ -6.62381620e-01,  -4.64756684e-01,  -8.09165116e-01]])
pp = array([ 0.22940569,  2.99121598,  0.39148632])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011431417710410785
Q = array([ 19.81341388, -29.65817393,  -3.88162186])
E = -853.64912038671275
hkl_projection = array([-0.87339254,  0.66020795,  0.62463026])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
