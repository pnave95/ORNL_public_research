#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E118.684265372_hkl-9.0308785136,2.8220698514,-0.172984658253/sample/sampleassembly.xml'
psi = -0.004022478602731029
hkl2Q = array([[-0.65691684,  0.9369934 ,  0.        ],
       [ 0.66255439,  0.46451035, -0.80916512],
       [-0.66255439, -0.46451035, -0.80916512]])
pp = array([ 1.20672297,  2.74660148,  0.83266443])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0025848240591527312
Q = array([ 7.91692268, -7.07063976, -2.14354733])
E = 118.68426537214026
hkl_projection = array([ 0.93396162, -0.99515405,  0.45425693])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
