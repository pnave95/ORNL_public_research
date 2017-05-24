#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-42.9805381434_hkl-6.70322086944,-0.10361844829,1.04026776783/sample/sampleassembly.xml'
psi = -0.0025687456238977667
hkl2Q = array([[-0.65827828,  0.93603743,  0.        ],
       [ 0.66187842,  0.46547304, -0.80916512],
       [-0.66187842, -0.46547304, -0.80916512]])
pp = array([ 0.74750861,  2.90537965,  0.32349443])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0046987858178937601
Q = array([ 3.65547113, -6.80691384, -0.75790396])
E = -42.980538143422592
hkl_projection = array([-0.61076881, -0.48208506, -0.91856835])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
