#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-275.263444396_hkl-6.9444944745,-5.48697368081,2.52518618251/sample/sampleassembly.xml'
psi = 0.00032621394328344886
hkl2Q = array([[-0.66098531,  0.93412782,  0.        ],
       [ 0.66052812,  0.4673872 , -0.80916512],
       [-0.66052812, -0.4673872 , -0.80916512]])
pp = array([ 2.54131113,  1.59428283, -0.37342488])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016382397091196754
Q = array([ -0.70204803, -10.23182644,   2.39657513])
E = -275.26344439592935
hkl_projection = array([-0.4062568 , -0.31865522,  0.85975506])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
