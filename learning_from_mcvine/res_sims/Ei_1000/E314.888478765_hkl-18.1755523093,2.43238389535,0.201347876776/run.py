#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E314.888478765_hkl-18.1755523093,2.43238389535,0.201347876776/sample/sampleassembly.xml'
psi = -0.004582424740027961
hkl2Q = array([[-0.65639207,  0.93736109,  0.        ],
       [ 0.66281439,  0.46413928, -0.80916512],
       [-0.66281439, -0.46413928, -0.80916512]])
pp = array([ 1.43030657,  2.63708611,  0.35121343])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012447036855063104
Q = array([ 13.40905119, -16.00154414,  -2.13112388])
E = 314.88847876485215
hkl_projection = array([ 0.39395853,  0.85809047, -0.21574715])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
