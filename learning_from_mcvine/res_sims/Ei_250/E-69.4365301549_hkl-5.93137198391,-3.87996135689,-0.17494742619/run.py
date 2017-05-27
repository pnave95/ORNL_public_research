#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-69.4365301549_hkl-5.93137198391,-3.87996135689,-0.17494742619/sample/sampleassembly.xml'
psi = -0.000722294182650983
hkl2Q = array([[-0.66000551,  0.93482036,  0.        ],
       [ 0.66101781,  0.46669437, -0.80916512],
       [-0.66101781, -0.46669437, -0.80916512]])
pp = array([ 2.3872853 ,  1.81682936, -0.81953303])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023645695483849863
Q = array([ 1.46565797, -7.27387642,  3.28109074])
E = -69.43653015488573
hkl_projection = array([-0.09834639, -0.53634763,  0.02255782])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
