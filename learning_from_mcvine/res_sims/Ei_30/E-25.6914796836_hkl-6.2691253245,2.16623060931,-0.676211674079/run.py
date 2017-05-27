#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-25.6914796836_hkl-6.2691253245,2.16623060931,-0.676211674079/sample/sampleassembly.xml'
psi = -0.004899752229938509
hkl2Q = array([[-0.65609459,  0.93756934,  0.        ],
       [ 0.66296164,  0.46392893, -0.80916512],
       [-0.66296164, -0.46392893, -0.80916512]])
pp = array([-1.29342102,  2.70685464,  0.7158461 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0066311452487154178
Q = array([ 5.99756938, -4.55904847, -1.20567135])
E = -25.691479683646641
hkl_projection = array([ 0.54927856,  0.69941515, -0.05399932])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
