#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E94.4896161273_hkl-6.92163054243,2.43856144207,-3.73000271606/sample/sampleassembly.xml'
psi = -0.011449433073373677
hkl2Q = array([[-0.64993978,  0.94184641,  0.        ],
       [ 0.66598598,  0.45957683, -0.80916512],
       [-0.66598598, -0.45957683, -0.80916512]])
pp = array([-0.63839933,  2.93128748, -0.83143623])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0040474398371056451
Q = array([ 8.60682028, -3.68418373,  1.04498923])
E = 94.489616127252901
hkl_projection = array([ 0.98079335,  0.47867689,  0.64110041])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
