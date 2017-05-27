#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E328.043814846_hkl-19.140330656,5.63204767275,1.28614636665/sample/sampleassembly.xml'
psi = -0.005299316768154029
hkl2Q = array([[-0.65571992,  0.93783142,  0.        ],
       [ 0.66314695,  0.463664  , -0.80916512],
       [-0.66314695, -0.463664  , -0.80916512]])
pp = array([ 1.15615324,  2.76826835,  0.97246964])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.001258865455161089
Q = array([ 15.43266722, -15.93536541,  -5.59796129])
E = 328.0438148459782
hkl_projection = array([-0.00953726, -0.63219495, -0.30461839])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
