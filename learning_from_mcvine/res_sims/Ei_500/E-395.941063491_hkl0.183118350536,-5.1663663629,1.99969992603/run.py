#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-395.941063491_hkl0.183118350536,-5.1663663629,1.99969992603/sample/sampleassembly.xml'
psi = 0.007192886269505729
hkl2Q = array([[-0.66738403,  0.92956707,  0.        ],
       [ 0.65730318,  0.47191177, -0.80916512],
       [-0.65730318, -0.47191177, -0.80916512]])
pp = array([ 2.96364227,  0.4656442 , -0.37151953])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016210473618907002
Q = array([-4.83248839, -3.21153025,  2.56235602])
E = -395.94106349128879
hkl_projection = array([ 0.38453922, -0.37772981, -0.94511177])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
