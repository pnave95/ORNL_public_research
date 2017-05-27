#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-404.491404653_hkl-10.1086004781,-2.70051517309,6.89820943227/sample/sampleassembly.xml'
psi = -0.00011443389861833567
hkl2Q = array([[-0.66057363,  0.93441899,  0.        ],
       [ 0.66073401,  0.46709609, -0.80916512],
       [-0.66073401, -0.46709609, -0.80916512]])
pp = array([ 2.21655038,  2.02160936,  0.49296851])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016212749743430869
Q = array([  0.3352711 , -13.92919502,  -3.39662776])
E = -404.49140465321949
hkl_projection = array([-0.81662935,  0.03326008, -0.46898794])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
