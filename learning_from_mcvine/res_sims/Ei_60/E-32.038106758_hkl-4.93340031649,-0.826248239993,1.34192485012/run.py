#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-32.038106758_hkl-4.93340031649,-0.826248239993,1.34192485012/sample/sampleassembly.xml'
psi = -0.001545427726495121
hkl2Q = array([[-0.6592358 ,  0.93536331,  0.        ],
       [ 0.66140174,  0.46615011, -0.80916512],
       [-0.66140174, -0.46615011, -0.80916512]])
pp = array([ 1.61346079,  2.52917858,  0.18760953])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047349770013302133
Q = array([ 1.81824066, -5.62521578, -0.41726752])
E = -32.038106758044741
hkl_projection = array([-0.96782457, -0.36777261, -0.16099685])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
