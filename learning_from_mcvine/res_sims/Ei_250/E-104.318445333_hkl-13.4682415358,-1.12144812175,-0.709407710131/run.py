#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-104.318445333_hkl-13.4682415358,-1.12144812175,-0.709407710131/sample/sampleassembly.xml'
psi = -0.0024093901869210537
hkl2Q = array([[-0.65842744,  0.93593252,  0.        ],
       [ 0.66180423,  0.46557851, -0.80916512],
       [-0.66180423, -0.46557851, -0.80916512]])
pp = array([ 0.55926602,  2.94740929, -0.34120604])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023336654732525669
Q = array([  8.59516968, -12.79720239,   1.48146467])
E = -104.31844533255884
hkl_projection = array([-0.74546497,  0.22154842,  0.37803131])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
