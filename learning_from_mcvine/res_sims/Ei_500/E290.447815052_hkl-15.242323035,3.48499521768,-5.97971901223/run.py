#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E290.447815052_hkl-15.242323035,3.48499521768,-5.97971901223/sample/sampleassembly.xml'
psi = -0.007814859482553073
hkl2Q = array([[-0.65335869,  0.93947794,  0.        ],
       [ 0.66431122,  0.46199436, -0.80916512],
       [-0.66431122, -0.46199436, -0.80916512]])
pp = array([-0.19219584,  2.99383713, -0.607558  ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0018687865887791447
Q = array([ 16.24622005,  -9.94718163,   2.01864347])
E = 290.44781505167953
hkl_projection = array([-0.31659184,  0.05119446,  0.1722213 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
