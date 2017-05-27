#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-14.618223859_hkl-2.6101179329,-2.52552526813,-0.658617753261/sample/sampleassembly.xml'
psi = -0.0005296639204882262
hkl2Q = array([[-0.66018557,  0.9346932 ,  0.        ],
       [ 0.6609279 ,  0.46682169, -0.80916512],
       [-0.6609279 , -0.46682169, -0.80916512]])
pp = array([ 2.86194691,  0.89958874, -0.69999015])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023993654708981413
Q = array([ 0.48927093, -3.31117242,  2.57649746])
E = -14.618223858980969
hkl_projection = array([ 0.30778381, -0.28024846, -0.68019685])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
