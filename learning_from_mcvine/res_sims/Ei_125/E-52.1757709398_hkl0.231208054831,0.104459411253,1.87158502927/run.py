#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-52.1757709398_hkl0.231208054831,0.104459411253,1.87158502927/sample/sampleassembly.xml'
psi = 0.010308272392096321
hkl2Q = array([[-0.67027674,  0.9274834 ,  0.        ],
       [ 0.6558298 ,  0.47395723, -0.80916512],
       [-0.6558298 , -0.47395723, -0.80916512]])
pp = array([ 2.99301998,  0.20452719,  0.52484   ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0033050898244528057
Q = array([-1.31390703, -0.62310033, -1.59894623])
E = -52.175770939782765
hkl_projection = array([-0.00703989, -0.60073381,  0.25503184])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
