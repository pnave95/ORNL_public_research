#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E17.5905156356_hkl-2.28307077532,0.30995561062,-0.559599278051/sample/sampleassembly.xml'
psi = -0.004449223870330697
hkl2Q = array([[-0.65651692,  0.93727365,  0.        ],
       [ 0.66275256,  0.46422757, -0.80916512],
       [-0.66275256, -0.46422757, -0.80916512]])
pp = array([ 2.12603687,  2.1165933 , -0.24626216])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0076243913858071461
Q = array([ 2.07517432, -1.73619074,  0.20200295])
E = 17.590515635592226
hkl_projection = array([-0.55476096, -0.49563641, -0.26267781])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
