#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-7.41656814747_hkl-8.30912697632,1.09972037162,0.72653894578/sample/sampleassembly.xml'
psi = -0.00363215599968495
hkl2Q = array([[-0.65728252,  0.93673692,  0.        ],
       [ 0.66237303,  0.46476893, -0.80916512],
       [-0.66237303, -0.46476893, -0.80916512]])
pp = array([ 0.79655191,  2.89231828,  0.56164218])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0033874023801451162
Q = array([ 5.70862923, -7.6100229 , -1.47774533])
E = -7.4165681474740808
hkl_projection = array([-0.95175129,  0.58431801,  0.85420568])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
