#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E6.1041419042_hkl-4.74564527349,1.05229812468,-1.65846465771/sample/sampleassembly.xml'
psi = -0.005726824585326188
hkl2Q = array([[-0.65531893,  0.93811165,  0.        ],
       [ 0.66334511,  0.46338046, -0.80916512],
       [-0.66334511, -0.46338046, -0.80916512]])
pp = array([-0.96761045,  2.83967076, -0.4358262 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0070993984810298122
Q = array([ 4.90808241, -3.19583065,  0.49048881])
E = 6.1041419042043472
hkl_projection = array([-0.71920032,  0.94540947,  0.50617445])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
