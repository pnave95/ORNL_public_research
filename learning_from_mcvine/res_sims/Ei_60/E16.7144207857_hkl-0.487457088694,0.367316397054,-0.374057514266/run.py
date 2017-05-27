#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E16.7144207857_hkl-0.487457088694,0.367316397054,-0.374057514266/sample/sampleassembly.xml'
psi = -0.031673063238265735
hkl2Q = array([[-0.63076062,  0.95479705,  0.        ],
       [ 0.67514347,  0.44601511, -0.80916512],
       [-0.67514347, -0.44601511, -0.80916512]])
pp = array([ 2.99871282,  0.08787164, -0.00355681])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0050565230575099207
Q = array([ 0.80800249, -0.13475863,  0.00545468])
E = 16.714420785725792
hkl_projection = array([-0.96315834,  0.87502632,  0.90903994])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
