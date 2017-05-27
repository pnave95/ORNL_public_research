#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-375.721656243_hkl-28.6250233161,6.8717384023,2.3909030155/sample/sampleassembly.xml'
psi = -0.004805904519361527
hkl2Q = array([[-0.65618257,  0.93750776,  0.        ],
       [ 0.6629181 ,  0.46399115, -0.80916512],
       [-0.6629181 , -0.46399115, -0.80916512]])
pp = array([ 0.04050872,  2.99972649,  0.90814177])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011753990193051731
Q = array([ 21.75366832, -24.75711356,  -7.49500632])
E = -375.72165624286606
hkl_projection = array([-0.26319812,  0.73989778, -0.09287124])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
