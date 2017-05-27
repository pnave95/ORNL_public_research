#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E36.8840065466_hkl-8.27267759906,2.8008447824,-0.416234134351/sample/sampleassembly.xml'
psi = -0.005845749724036546
hkl2Q = array([[-0.65520736,  0.93818958,  0.        ],
       [ 0.66340022,  0.46330156, -0.80916512],
       [-0.66340022, -0.46330156, -0.80916512]])
pp = array([ 0.11946723,  2.99762032,  0.9223675 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0035429825387334577
Q = array([ 7.55453006, -6.27086225, -1.92954375])
E = 36.884006546564422
hkl_projection = array([ 0.62869175,  0.96405724, -0.25726164])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
