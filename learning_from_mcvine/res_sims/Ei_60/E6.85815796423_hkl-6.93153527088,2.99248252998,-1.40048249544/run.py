#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E6.85815796423_hkl-6.93153527088,2.99248252998,-1.40048249544/sample/sampleassembly.xml'
psi = -0.0079912732743933
hkl2Q = array([[-0.65319294,  0.93959318,  0.        ],
       [ 0.66439271,  0.46187716, -0.80916512],
       [-0.66439271, -0.46187716, -0.80916512]])
pp = array([-1.24211731,  2.73077729,  0.78454707])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0049881696699460853
Q = array([ 7.44628386, -4.4838131 , -1.28819089])
E = 6.8581579642320776
hkl_projection = array([-0.05815326, -0.18926027, -0.28366131])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
