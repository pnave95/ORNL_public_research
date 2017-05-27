#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-57.6332255054_hkl-2.64410283193,-3.1244083832,0.0911222647501/sample/sampleassembly.xml'
psi = 0.000457285979698073
hkl2Q = array([[-0.66110774,  0.93404118,  0.        ],
       [ 0.66046685,  0.46747377, -0.80916512],
       [-0.66046685, -0.46747377, -0.80916512]])
pp = array([ 2.69856923,  1.31061974, -0.8096962 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0033077114900657866
Q = array([-0.37571454, -3.97287715,  2.45442932])
E = -57.633225505408618
hkl_projection = array([ 0.03537302,  0.46855329, -0.05625054])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
