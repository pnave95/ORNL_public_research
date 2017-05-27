#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-16.9473905936_hkl-5.32927591883,0.474639205385,-0.0253877791861/sample/sampleassembly.xml'
psi = -0.002998013990579733
hkl2Q = array([[ -6.57876411e-01,   9.36319923e-01,  -7.76354847e-17],
       [  6.62078167e-01,   4.65188872e-01,  -8.09165116e-01],
       [ -6.62078167e-01,  -4.65188872e-01,  -8.09165116e-01]])
pp = array([-0.01131966,  2.99997864,  0.22923674])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0066897088329371628
Q = array([ 3.83706187, -4.75730023, -0.36351858])
E = -16.947390593601419
hkl_projection = array([ 0.14385011, -0.88182061, -0.49421885])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
