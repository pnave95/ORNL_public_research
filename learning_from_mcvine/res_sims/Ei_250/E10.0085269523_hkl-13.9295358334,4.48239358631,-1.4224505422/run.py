#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E10.0085269523_hkl-13.9295358334,4.48239358631,-1.4224505422/sample/sampleassembly.xml'
psi = -0.004550072103487711
hkl2Q = array([[-0.6564224 ,  0.93733986,  0.        ],
       [ 0.66279937,  0.46416073, -0.80916512],
       [-0.66279937, -0.46416073, -0.80916512]])
pp = array([-0.58033154,  2.94333405,  0.70645159])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0024210244334135385
Q = array([ 13.05738626, -10.31591238,  -2.47599917])
E = 10.008526952300741
hkl_projection = array([-0.82636499,  0.91470978,  0.28553474])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
