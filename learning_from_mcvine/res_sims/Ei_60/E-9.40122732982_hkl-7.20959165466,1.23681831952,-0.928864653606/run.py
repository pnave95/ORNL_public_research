#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-9.40122732982_hkl-7.20959165466,1.23681831952,-0.928864653606/sample/sampleassembly.xml'
psi = -0.005133259019743075
hkl2Q = array([[-0.65587564,  0.93772252,  0.        ],
       [ 0.66306995,  0.46377411, -0.80916512],
       [-0.66306995, -0.46377411, -0.80916512]])
pp = array([-0.39157467,  2.9743351 ,  0.1287585 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0048415540386056791
Q = array([ 6.16459485, -5.75620872, -0.24918536])
E = -9.4012273298248559
hkl_projection = array([ 0.41656108, -0.71270703,  0.40234265])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
