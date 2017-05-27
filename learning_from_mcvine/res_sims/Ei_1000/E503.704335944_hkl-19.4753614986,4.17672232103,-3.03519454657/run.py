#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E503.704335944_hkl-19.4753614986,4.17672232103,-3.03519454657/sample/sampleassembly.xml'
psi = -0.006430334656652332
hkl2Q = array([[-0.65465879,  0.93857245,  0.        ],
       [ 0.66367094,  0.46291367, -0.80916512],
       [-0.66367094, -0.46291367, -0.80916512]])
pp = array([ 0.87433105,  2.86976397,  0.17742035])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012880264940516961
Q = array([ 17.5360563 , -14.94054277,  -0.92368445])
E = 503.70433594394422
hkl_projection = array([-0.33691293, -0.54658926, -0.11929548])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
