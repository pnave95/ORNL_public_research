#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-29.3278557978_hkl-2.21336468781,-0.610795227345,1.93360910552/sample/sampleassembly.xml'
psi = 0.00031948010838024794
hkl2Q = array([[-0.66097902,  0.93413227,  0.        ],
       [ 0.66053127,  0.46738275, -0.80916512],
       [-0.66053127, -0.46738275, -0.80916512]])
pp = array([ 2.59617416,  1.50328964,  0.49407096])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047539921548166155
Q = array([-0.21767099, -3.25678608, -1.07037485])
E = -29.327855797823066
hkl_projection = array([-0.23024232, -0.90118394, -0.28504223])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
