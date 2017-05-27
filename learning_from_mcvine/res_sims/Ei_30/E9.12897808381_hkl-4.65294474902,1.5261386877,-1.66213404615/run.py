#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E9.12897808381_hkl-4.65294474902,1.5261386877,-1.66213404615/sample/sampleassembly.xml'
psi = -0.006664447131068248
hkl2Q = array([[-0.65443904,  0.93872568,  0.        ],
       [ 0.6637793 ,  0.46275829, -0.80916512],
       [-0.6637793 , -0.46275829, -0.80916512]])
pp = array([-1.26282971,  2.72126094, -0.10353023])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0071824069005289141
Q = array([ 5.16137814, -2.89243912,  0.1100427 ])
E = 9.1289780838081498
hkl_projection = array([ 0.82414179, -0.28854987, -0.46074425])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
