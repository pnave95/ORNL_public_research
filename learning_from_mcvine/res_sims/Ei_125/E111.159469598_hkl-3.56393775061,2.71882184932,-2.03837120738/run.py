#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E111.159469598_hkl-3.56393775061,2.71882184932,-2.03837120738/sample/sampleassembly.xml'
psi = -0.022618807359480513
hkl2Q = array([[-0.63937962,  0.94904693,  0.        ],
       [ 0.67107752,  0.45210967, -0.80916512],
       [-0.67107752, -0.45210967, -0.80916512]])
pp = array([ 2.65310257,  1.4003738 ,  0.62606328])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0045897047514698629
Q = array([ 5.47115448, -1.23157121, -0.55059692])
E = 111.15946959840753
hkl_projection = array([ 0.67807298, -0.20424885, -0.61234821])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
