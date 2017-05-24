#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E12.1835030023_hkl-4.86821206102,0.430926155696,0.0723533741666/sample/sampleassembly.xml'
psi = -0.0037442409033065487
hkl2Q = array([[-0.65717752,  0.93681059,  0.        ],
       [ 0.66242512,  0.46469468, -0.80916512],
       [-0.66242512, -0.46469468, -0.80916512]])
pp = array([ 1.2273064 ,  2.7374658 ,  0.25371051])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0050103664691109519
Q = array([ 3.43680715, -4.39396574, -0.40723624])
E = 12.183503002291573
hkl_projection = array([-0.43152037, -0.30816576,  0.15283546])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
