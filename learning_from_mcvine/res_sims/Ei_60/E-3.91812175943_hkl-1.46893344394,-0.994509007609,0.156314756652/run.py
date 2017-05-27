#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-3.91812175943_hkl-1.46893344394,-0.994509007609,0.156314756652/sample/sampleassembly.xml'
psi = -0.0005234220629938785
hkl2Q = array([[-0.6601914 ,  0.93468908,  0.        ],
       [ 0.66092499,  0.46682582, -0.80916512],
       [-0.66092499, -0.46682582, -0.80916512]])
pp = array([ 2.81585097,  1.03488324, -0.36744086])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0048813249466707004
Q = array([ 0.20916905, -1.9102303 ,  0.67823755])
E = -3.9181217594325304
hkl_projection = array([-0.80589674, -0.24110094, -0.67125828])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
