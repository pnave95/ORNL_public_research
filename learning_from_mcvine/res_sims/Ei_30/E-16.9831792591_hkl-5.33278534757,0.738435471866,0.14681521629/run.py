#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-16.9831792591_hkl-5.33278534757,0.738435471866,0.14681521629/sample/sampleassembly.xml'
psi = -0.0030723180580274475
hkl2Q = array([[-0.65780684,  0.9363688 ,  0.        ],
       [ 0.66211273,  0.46513968, -0.80916512],
       [-0.66211273, -0.46513968, -0.80916512]])
pp = array([-0.05120873,  2.99956291,  0.4553851 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0066978544341085682
Q = array([ 3.89966197, -4.71826778, -0.71631398])
E = -16.983179259051397
hkl_projection = array([-0.59759489, -0.66052787,  0.94496401])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
