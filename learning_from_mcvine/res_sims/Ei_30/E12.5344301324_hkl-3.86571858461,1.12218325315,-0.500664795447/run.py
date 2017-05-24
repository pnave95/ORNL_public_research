#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E12.5344301324_hkl-3.86571858461,1.12218325315,-0.500664795447/sample/sampleassembly.xml'
psi = -0.004686013938478748
hkl2Q = array([[-0.65629497,  0.93742908,  0.        ],
       [ 0.66286246,  0.46407062, -0.80916512],
       [-0.66286246, -0.46407062, -0.80916512]])
pp = array([ 0.21507187,  2.99228075,  0.52420667])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0073436560040032435
Q = array([ 3.6127767 , -2.87072093, -0.50291106])
E = 12.534430132404744
hkl_projection = array([-0.15563475, -0.8171971 ,  0.26221998])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
