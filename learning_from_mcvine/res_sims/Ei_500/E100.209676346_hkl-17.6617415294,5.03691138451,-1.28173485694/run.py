#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E100.209676346_hkl-17.6617415294,5.03691138451,-1.28173485694/sample/sampleassembly.xml'
psi = -0.005514792442646018
hkl2Q = array([[-0.65551782,  0.93797269,  0.        ],
       [ 0.66324685,  0.4635211 , -0.80916512],
       [-0.66324685, -0.4635211 , -0.80916512]])
pp = array([-0.03536408,  2.99979156,  0.66838522])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017401292118785704
Q = array([ 15.76840851, -13.6374053 ,  -3.03855785])
E = 100.20967634613226
hkl_projection = array([-0.78306803, -0.69858484, -0.5276171 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
