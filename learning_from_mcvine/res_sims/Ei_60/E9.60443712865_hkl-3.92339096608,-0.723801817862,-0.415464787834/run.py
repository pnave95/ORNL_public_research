#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E9.60443712865_hkl-3.92339096608,-0.723801817862,-0.415464787834/sample/sampleassembly.xml'
psi = -0.0029795562240654944
hkl2Q = array([[-0.65789369,  0.93630778,  0.        ],
       [ 0.66206958,  0.46520109, -0.80916512],
       [-0.66206958, -0.46520109, -0.80916512]])
pp = array([ 1.86513676,  2.34973719, -0.56750077])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.004998616277144147
Q = array([ 2.37703361, -3.81694021,  0.9218548 ])
E = 9.6044371286468504
hkl_projection = array([ 0.98845245,  0.53614045,  0.82072211])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
