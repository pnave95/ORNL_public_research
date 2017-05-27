#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-16.4074366968_hkl-7.44500973674,-0.885319390662,0.155738053457/sample/sampleassembly.xml'
psi = -0.0027334548815738063
hkl2Q = array([[-0.6581241 ,  0.93614584,  0.        ],
       [ 0.66195507,  0.46536401, -0.80916512],
       [-0.66195507, -0.46536401, -0.80916512]])
pp = array([ 1.30287048,  2.7023191 , -0.21401939])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0033595469656690501
Q = array([ 4.21060708, -7.45408559,  0.59035177])
E = -16.407436696770887
hkl_projection = array([ 0.64801809,  0.27488746, -0.2899562 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
