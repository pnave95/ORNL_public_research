#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-38.9339473314_hkl-5.92481503782,-0.236086279474,2.33669850272/sample/sampleassembly.xml'
psi = -0.0015812589487817737
hkl2Q = array([[-0.65920229,  0.93538693,  0.        ],
       [ 0.66141844,  0.46612641, -0.80916512],
       [-0.66141844, -0.46612641, -0.80916512]])
pp = array([ 1.9170737 ,  2.30755898,  0.58183015])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0033274266814317124
Q = array([ 2.20396431, -6.7412375 , -1.69974213])
E = -38.933947331431909
hkl_projection = array([ 0.6360175 ,  0.17699346,  0.53219928])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
