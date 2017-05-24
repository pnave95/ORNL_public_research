#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-54.5559885646_hkl-15.0989488937,-1.36498428307,3.66609517212/sample/sampleassembly.xml'
psi = -0.002192903974961433
hkl2Q = array([[-0.65863004,  0.93578996,  0.        ],
       [ 0.66170342,  0.46572177, -0.80916512],
       [-0.66170342, -0.46572177, -0.80916512]])
pp = array([ 2.05390369,  2.18665947,  0.24716991])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011937903593590674
Q = array([  6.61553879, -16.47252795,  -1.86197866])
E = -54.55598856458414
hkl_projection = array([-0.739556  , -0.97178612,  0.61179289])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
