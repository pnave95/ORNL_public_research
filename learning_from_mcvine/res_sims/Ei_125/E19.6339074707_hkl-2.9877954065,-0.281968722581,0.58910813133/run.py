#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E19.6339074707_hkl-2.9877954065,-0.281968722581,0.58910813133/sample/sampleassembly.xml'
psi = -0.0021029565170895357
hkl2Q = array([[-0.65871421,  0.93573071,  0.        ],
       [ 0.66166153,  0.46578128, -0.80916512],
       [-0.66166153, -0.46578128, -0.80916512]])
pp = array([ 2.68409288,  1.34001695,  0.10402292])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0034485370387488659
Q = array([ 1.39174524, -3.20150322, -0.2485265 ])
E = 19.63390747067811
hkl_projection = array([ 0.17665989,  0.28648719, -0.99661365])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
