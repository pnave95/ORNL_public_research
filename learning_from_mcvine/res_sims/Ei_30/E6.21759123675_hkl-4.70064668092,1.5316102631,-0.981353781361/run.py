#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E6.21759123675_hkl-4.70064668092,1.5316102631,-0.981353781361/sample/sampleassembly.xml'
psi = -0.0054558814495611055
hkl2Q = array([[-0.65557308,  0.93793407,  0.        ],
       [ 0.66321954,  0.46356017, -0.80916512],
       [-0.66321954, -0.46356017, -0.80916512]])
pp = array([-0.8260533 ,  2.8840312 ,  0.39584323])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0071001677475798185
Q = array([ 4.74826426, -3.24398662, -0.44524835])
E = 6.2175912367512112
hkl_projection = array([ 0.54248662,  0.49174728, -0.8922922 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
