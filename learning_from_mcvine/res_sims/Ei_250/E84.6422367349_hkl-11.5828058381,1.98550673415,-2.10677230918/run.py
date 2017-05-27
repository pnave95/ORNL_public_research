#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E84.6422367349_hkl-11.5828058381,1.98550673415,-2.10677230918/sample/sampleassembly.xml'
psi = -0.004141117390418237
hkl2Q = array([[-0.65680567,  0.93707133,  0.        ],
       [ 0.66260949,  0.46443174, -0.80916512],
       [-0.66260949, -0.46443174, -0.80916512]])
pp = array([ 0.23522445,  2.99076403, -0.03277723])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0024984033518645915
Q = array([ 10.31923551,  -8.953331  ,   0.09812387])
E = 84.642236734863729
hkl_projection = array([ 0.99461886, -0.65654657,  0.66699535])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
