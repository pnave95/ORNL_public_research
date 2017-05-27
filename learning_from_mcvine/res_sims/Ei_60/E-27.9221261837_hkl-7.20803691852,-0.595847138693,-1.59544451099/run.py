#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-27.9221261837_hkl-7.20803691852,-0.595847138693,-1.59544451099/sample/sampleassembly.xml'
psi = -0.004108482715229388
hkl2Q = array([[-0.65683625,  0.9370499 ,  0.        ],
       [ 0.66259434,  0.46445337, -0.80916512],
       [-0.66259434, -0.46445337, -0.80916512]])
pp = array([ 0.00474836,  2.99999624, -0.8456794 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047783850067576617
Q = array([ 5.39682751, -6.29002389,  1.77311676])
E = -27.922126183689517
hkl_projection = array([-0.43638993,  0.41007124, -0.97457522])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
