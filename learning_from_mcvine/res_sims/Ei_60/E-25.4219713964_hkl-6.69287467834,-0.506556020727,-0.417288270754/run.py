#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-25.4219713964_hkl-6.69287467834,-0.506556020727,-0.417288270754/sample/sampleassembly.xml'
psi = -0.003293284228766529
hkl2Q = array([[ -6.57599915e-01,   9.36514134e-01,   7.76193850e-17],
       [  6.62215495e-01,   4.64993360e-01,  -8.09165116e-01],
       [ -6.62215495e-01,  -4.64993360e-01,  -8.09165116e-01]])
pp = array([ 0.49916448,  2.958181  , -0.35048308])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047655230978895548
Q = array([ 4.34211934, -6.30948064,  0.74754257])
E = -25.421971396382055
hkl_projection = array([-0.3804329 ,  0.53747577,  0.96238327])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
