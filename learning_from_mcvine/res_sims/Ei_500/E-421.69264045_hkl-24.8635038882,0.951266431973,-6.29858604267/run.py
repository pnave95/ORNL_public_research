#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-421.69264045_hkl-24.8635038882,0.951266431973,-6.29858604267/sample/sampleassembly.xml'
psi = -0.005045467704500159
hkl2Q = array([[-0.65595796,  0.93766493,  0.        ],
       [ 0.66302923,  0.46383232, -0.80916512],
       [-0.66302923, -0.46383232, -0.80916512]])
pp = array([-0.79845186,  2.89179436, -0.62715917])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016209743632139516
Q = array([ 21.11627746, -19.95091975,   4.3268645 ])
E = -421.69264044969054
hkl_projection = array([ 0.0832452 ,  0.57028309,  0.35239957])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
