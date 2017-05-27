#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-801.182777371_hkl-35.0759853007,11.2982355067,-1.69638146715/sample/sampleassembly.xml'
psi = -0.0064317124081528605
hkl2Q = array([[-0.6546575 ,  0.93857335,  0.        ],
       [ 0.66367158,  0.46291276, -0.80916512],
       [-0.66367158, -0.46291276, -0.80916512]])
pp = array([-0.99871127,  2.82888243,  0.81687919])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011499443371344349
Q = array([ 31.58691479, -26.906011  ,  -7.76948534])
E = -801.18277737112055
hkl_projection = array([ 0.34054681,  0.43486313, -0.11810244])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
