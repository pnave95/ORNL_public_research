#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E288.732452146_hkl-9.4914895403,2.80075088567,-0.783412585546/sample/sampleassembly.xml'
psi = -0.005662957870312823
hkl2Q = array([[-0.65537884,  0.9380698 ,  0.        ],
       [ 0.66331552,  0.46342282, -0.80916512],
       [-0.66331552, -0.46342282, -0.80916512]])
pp = array([ 2.08636041,  2.15571339,  0.48585493])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0018634916753288893
Q = array([ 8.59795263, -7.24269655, -1.63235978])
E = 288.7324521458961
hkl_projection = array([-0.1098081 ,  0.61520001,  0.76443317])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
