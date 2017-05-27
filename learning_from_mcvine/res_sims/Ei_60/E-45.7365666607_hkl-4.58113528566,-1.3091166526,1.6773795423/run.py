#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-45.7365666607_hkl-4.58113528566,-1.3091166526,1.6773795423/sample/sampleassembly.xml'
psi = -0.0008830118993015397
hkl2Q = array([[-0.65985526,  0.93492642,  0.        ],
       [ 0.66109281,  0.46658813, -0.80916512],
       [-0.66109281, -0.46658813, -0.80916512]])
pp = array([ 1.82695062,  2.37954858,  0.12491367])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0046866611673501424
Q = array([ 1.04853504, -5.67648808, -0.29798548])
E = -45.736566660735917
hkl_projection = array([-0.01268556, -0.14270754,  0.49436058])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
