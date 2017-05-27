#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-21.6580999686_hkl0.0685558770047,-1.36920734393,-0.334507937661/sample/sampleassembly.xml'
psi = 0.008210841116233174
hkl2Q = array([[-0.66832994,  0.92888722,  0.        ],
       [ 0.65682245,  0.47258063, -0.80916512],
       [-0.65682245, -0.47258063, -0.80916512]])
pp = array([ 2.9928108 ,  0.20756564, -0.67281561])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047960180402308221
Q = array([-0.72543174, -0.42529822,  1.37858697])
E = -21.658099968562851
hkl_projection = array([ 0.777114  , -0.82266323, -0.82078192])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
