#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-302.048113998_hkl1.35567757273,-1.87830436017,1.4506733558/sample/sampleassembly.xml'
psi = 0.04659973919395292
hkl2Q = array([[-0.70348774,  0.9025527 ,  0.        ],
       [ 0.63820113,  0.49744095, -0.80916512],
       [-0.63820113, -0.49744095, -0.80916512]])
pp = array([ 2.99955728,  0.05153754, -0.0412425 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011722597168068679
Q = array([-3.0782599 , -0.43239938,  0.34602409])
E = -302.04811399849291
hkl_projection = array([ 0.36874081,  0.93874574, -0.99821803])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
