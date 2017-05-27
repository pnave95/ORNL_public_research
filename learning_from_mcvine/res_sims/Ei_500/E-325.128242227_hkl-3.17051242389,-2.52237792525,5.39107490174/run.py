#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-325.128242227_hkl-3.17051242389,-2.52237792525,5.39107490174/sample/sampleassembly.xml'
psi = 0.0022254022035460208
hkl2Q = array([[-0.6627582 ,  0.9328708 ,  0.        ],
       [ 0.65963927,  0.46864082, -0.80916512],
       [-0.65963927, -0.46864082, -0.80916512]])
pp = array([ 2.82626385,  1.00609772,  0.35033271])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016304701857176788
Q = array([-3.11874114, -6.66624549, -2.32124952])
E = -325.12824222733764
hkl_projection = array([-0.95915898,  0.82876032, -0.40509494])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
