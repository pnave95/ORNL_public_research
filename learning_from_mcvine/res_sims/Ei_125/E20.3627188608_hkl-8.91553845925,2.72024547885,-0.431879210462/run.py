#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E20.3627188608_hkl-8.91553845925,2.72024547885,-0.431879210462/sample/sampleassembly.xml'
psi = -0.005576612579576111
hkl2Q = array([[-0.65545983,  0.93801321,  0.        ],
       [ 0.6632755 ,  0.46348009, -0.80916512],
       [-0.6632755 , -0.46348009, -0.80916512]])
pp = array([-0.0565198 ,  2.99946754,  0.80470243])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.003473987570809506
Q = array([ 7.93450444, -6.90194578, -1.85166616])
E = 20.362718860812578
hkl_projection = array([-0.55150907,  0.95590348,  0.26319821])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
