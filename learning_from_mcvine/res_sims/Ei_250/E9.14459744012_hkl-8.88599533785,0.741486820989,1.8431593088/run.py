#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E9.14459744012_hkl-8.88599533785,0.741486820989,1.8431593088/sample/sampleassembly.xml'
psi = -0.0020819878463354917
hkl2Q = array([[-0.65873383,  0.9357169 ,  0.        ],
       [ 0.66165176,  0.46579516, -0.80916512],
       [-0.66165176, -0.46579516, -0.80916512]])
pp = array([ 1.66675003,  2.49438256,  0.59093871])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.002416634465631604
Q = array([ 5.12458219, -8.82792971, -2.09140549])
E = 9.1445974401152057
hkl_projection = array([ 0.11508405, -0.2574407 ,  0.58835801])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
