#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-114.364323521_hkl-3.7378306463,-1.30282650796,3.88637457648/sample/sampleassembly.xml'
psi = 0.0007798231334958275
hkl2Q = array([[-0.66140897,  0.9338279 ,  0.        ],
       [ 0.66031604,  0.46768677, -0.80916512],
       [-0.66031604, -0.46768677, -0.80916512]])
pp = array([ 2.48585217,  1.67944603,  0.59331865])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.003234528643394758
Q = array([-0.95427798, -5.91741123, -2.09051697])
E = -114.36432352102811
hkl_projection = array([ 0.15491073,  0.09203786, -0.61841924])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
