#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-45.4982055208_hkl-1.34660799819,-1.76169720396,1.40427651341/sample/sampleassembly.xml'
psi = 0.002088120569546855
hkl2Q = array([[-0.66263013,  0.93296178,  0.        ],
       [ 0.6597036 ,  0.46855026, -0.80916512],
       [-0.6597036 , -0.46855026, -0.80916512]])
pp = array([ 2.77094605,  1.14972084, -0.12136628])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0046873765092760866
Q = array([-1.19630123, -2.7397516 ,  0.28921235])
E = -45.498205520826993
hkl_projection = array([-0.50620173, -0.22752422,  0.19555835])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
