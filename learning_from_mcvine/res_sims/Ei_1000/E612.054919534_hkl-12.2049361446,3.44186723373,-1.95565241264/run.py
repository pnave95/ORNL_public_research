#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E612.054919534_hkl-12.2049361446,3.44186723373,-1.95565241264/sample/sampleassembly.xml'
psi = -0.007074704761671784
hkl2Q = array([[ -6.54053869e-01,   9.38994094e-01,   7.74143859e-17],
       [  6.63969091e-01,   4.62485926e-01,  -8.09165116e-01],
       [ -6.63969091e-01,  -4.62485926e-01,  -8.09165116e-01]])
pp = array([ 2.28358934,  1.94556411,  0.26101067])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0013276707833417506
Q = array([ 11.56647192,  -8.96408609,  -1.20259319])
E = 612.05491953447336
hkl_projection = array([-0.61296183,  0.89588173,  0.8401566 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
