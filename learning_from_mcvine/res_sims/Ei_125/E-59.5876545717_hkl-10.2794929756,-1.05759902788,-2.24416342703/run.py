#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-59.5876545717_hkl-10.2794929756,-1.05759902788,-2.24416342703/sample/sampleassembly.xml'
psi = -0.004021118003805631
hkl2Q = array([[-0.65691811,  0.93699251,  0.        ],
       [ 0.66255376,  0.46451125, -0.80916512],
       [-0.66255376, -0.46451125, -0.80916512]])
pp = array([ 0.08767709,  2.99871851, -0.88227188])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0033082521273703649
Q = array([ 7.53894785, -9.0806354 ,  2.671671  ])
E = -59.587654571745652
hkl_projection = array([-0.56993197,  0.58074568,  0.18492922])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
