#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E30.0447387339_hkl-1.81585703179,0.309291723975,-0.606753222658/sample/sampleassembly.xml'
psi = -0.006735774100849125
hkl2Q = array([[-0.65437208,  0.93877236,  0.        ],
       [ 0.6638123 ,  0.46271094, -0.80916512],
       [-0.6638123 , -0.46271094, -0.80916512]])
pp = array([ 2.82736144,  1.00300912, -0.18848955])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0052646431342041281
Q = array([ 1.79632806, -1.28081238,  0.24069547])
E = 30.04473873389648
hkl_projection = array([-0.61902432,  0.34499697,  0.46563449])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
