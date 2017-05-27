#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-12.7092677601_hkl-1.30261186484,-0.81752300643,0.885003291811/sample/sampleassembly.xml'
psi = 0.0004855989921112863
hkl2Q = array([[ -6.61134189e-01,   9.34022460e-01,  -7.78264488e-17],
       [  6.60453615e-01,   4.67492469e-01,  -8.09165116e-01],
       [ -6.60453615e-01,  -4.67492469e-01,  -8.09165116e-01]])
pp = array([ 2.69077643,  1.32654521,  0.03598997])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0067350044924625631
Q = array([-0.26323841, -2.01258696, -0.05460269])
E = -12.709267760053239
hkl_projection = array([-0.08650387,  0.65181745,  0.3870137 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
