#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E262.006677661_hkl-2.35459653487,4.9378866869,-0.819919950902/sample/sampleassembly.xml'
psi = 0.042091423444415334
hkl2Q = array([[-0.69941161,  0.90571506,  0.        ],
       [ 0.64043726,  0.49455869, -0.80916512],
       [-0.64043726, -0.49455869, -0.80916512]])
pp = array([ 2.99276089, -0.20828409,  0.97069395])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0018534460345786892
Q = array([ 5.33434607,  0.71497977, -3.33211503])
E = 262.00667766136746
hkl_projection = array([-0.86001119, -0.73927404,  0.82560331])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
