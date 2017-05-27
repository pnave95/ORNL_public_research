#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E20.0183689634_hkl-5.86876717951,1.60255055127,-0.830625519922/sample/sampleassembly.xml'
psi = -0.005980427082027559
hkl2Q = array([[-0.655081  ,  0.93827782,  0.        ],
       [ 0.66346261,  0.46321222, -0.80916512],
       [-0.66346261, -0.46321222, -0.80916512]])
pp = array([-0.03565663,  2.99978809,  0.42784117])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.005108778389530457
Q = array([ 5.45883919, -4.37945717, -0.62461481])
E = 20.018368963435975
hkl_projection = array([-0.65859949,  0.16444453,  0.73911406])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
