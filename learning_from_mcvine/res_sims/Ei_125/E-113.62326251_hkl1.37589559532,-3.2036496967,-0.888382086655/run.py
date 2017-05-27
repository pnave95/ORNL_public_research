#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-113.62326251_hkl1.37589559532,-3.2036496967,-0.888382086655/sample/sampleassembly.xml'
psi = -0.04529478400127958
hkl2Q = array([[-0.61769652,  0.96330025,  0.        ],
       [ 0.68115614,  0.4367774 , -0.80916512],
       [-0.68115614, -0.4367774 , -0.80916512]])
pp = array([ 2.9985869 , -0.09206841, -0.97041609])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.003249240250592643
Q = array([-2.42694468,  0.31414401,  3.31112937])
E = -113.62326251042447
hkl_projection = array([-0.2473328 ,  0.98970482, -0.83142884])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
