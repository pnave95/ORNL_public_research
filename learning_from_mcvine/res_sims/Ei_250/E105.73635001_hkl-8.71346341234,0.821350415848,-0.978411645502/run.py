#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E105.73635001_hkl-8.71346341234,0.821350415848,-0.978411645502/sample/sampleassembly.xml'
psi = -0.003392603761115019
hkl2Q = array([[-0.6575069 ,  0.93657944,  0.        ],
       [ 0.66226167,  0.46492759, -0.80916512],
       [-0.66226167, -0.46492759, -0.80916512]])
pp = array([ 1.46604148,  2.61738846, -0.04541722])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0025354537129469554
Q = array([ 6.92107574, -7.32409167,  0.12708847])
E = 105.73635000960127
hkl_projection = array([ 0.81823807,  0.40160131, -0.7158551 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
