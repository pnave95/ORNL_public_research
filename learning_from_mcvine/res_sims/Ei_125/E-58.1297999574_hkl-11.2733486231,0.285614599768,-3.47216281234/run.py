#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-58.1297999574_hkl-11.2733486231,0.285614599768,-3.47216281234/sample/sampleassembly.xml'
psi = -0.005427579273253794
hkl2Q = array([[-0.65559962,  0.93791551,  0.        ],
       [ 0.66320642,  0.46357894, -0.80916512],
       [-0.66320642, -0.46357894, -0.80916512]])
pp = array([-0.68729169,  2.92021063, -0.85259186])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0033089337957717567
Q = array([ 9.88298519, -8.83142208,  2.57844366])
E = -58.129799957432468
hkl_projection = array([-0.97171011,  0.76893081, -0.80678393])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
