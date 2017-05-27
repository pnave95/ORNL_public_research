#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E29.9727724102_hkl-9.71504760227,2.74236793015,-4.11604572438/sample/sampleassembly.xml'
psi = -0.008897825453636096
hkl2Q = array([[-0.65234088,  0.94018495,  0.        ],
       [ 0.66481116,  0.46127466, -0.80916512],
       [-0.66481116, -0.46127466, -0.80916512]])
pp = array([-1.37986034,  2.66382909, -0.49594112])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0034924034528355341
Q = array([ 10.89707263,  -5.97032912,   1.11153215])
E = 29.972772410162008
hkl_projection = array([ 0.96522777, -0.07513016, -0.02432215])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
