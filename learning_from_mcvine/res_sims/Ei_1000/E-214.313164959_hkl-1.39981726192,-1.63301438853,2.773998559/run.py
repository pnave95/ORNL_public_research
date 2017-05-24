#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-214.313164959_hkl-1.39981726192,-1.63301438853,2.773998559/sample/sampleassembly.xml'
psi = 0.003200319832054035
hkl2Q = array([[-0.66366736,  0.93222423,  0.        ],
       [ 0.65918207,  0.46928369, -0.80916512],
       [-0.65918207, -0.46928369, -0.80916512]])
pp = array([ 2.97095531,  0.41644271,  0.1139843 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011790429803196748
Q = array([-1.9760109 , -3.37308286, -0.92324459])
E = -214.31316495928729
hkl_projection = array([ 0.58813816,  0.72708305,  0.88905677])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
