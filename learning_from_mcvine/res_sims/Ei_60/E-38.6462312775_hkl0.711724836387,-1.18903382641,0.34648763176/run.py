#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-38.6462312775_hkl0.711724836387,-1.18903382641,0.34648763176/sample/sampleassembly.xml'
psi = 0.0684841933387731
hkl2Q = array([[-0.72306958,  0.88694236,  0.        ],
       [ 0.62716296,  0.5112874 , -0.80916512],
       [-0.62716296, -0.5112874 , -0.80916512]])
pp = array([ 2.99925132,  0.06701881, -0.29701311])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047128090062448086
Q = array([-1.47764876, -0.15383387,  0.68175899])
E = -38.64623127753535
hkl_projection = array([-0.43544159,  0.53167502,  0.43533407])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
