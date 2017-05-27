#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E170.650149188_hkl-7.90085892268,1.64899264707,-2.62215180027/sample/sampleassembly.xml'
psi = -0.005310944695553195
hkl2Q = array([[-0.65570901,  0.93783904,  0.        ],
       [ 0.66315234,  0.46365629, -0.80916512],
       [-0.66315234, -0.46365629, -0.80916512]])
pp = array([ 1.45471466,  2.62370068, -0.38052588])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0027353726940729808
Q = array([ 8.01308384, -5.42939097,  0.78744644])
E = 170.65014918803541
hkl_projection = array([-0.75804561, -0.86201325, -0.3002135 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
