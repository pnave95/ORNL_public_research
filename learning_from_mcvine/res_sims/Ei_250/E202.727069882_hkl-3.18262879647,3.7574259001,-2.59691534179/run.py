#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E202.727069882_hkl-3.18262879647,3.7574259001,-2.59691534179/sample/sampleassembly.xml'
psi = -0.08373702225004241
hkl2Q = array([[-0.58021786,  0.98632834,  0.        ],
       [ 0.69743946,  0.41027599, -0.80916512],
       [-0.69743946, -0.41027599, -0.80916512]])
pp = array([ 2.98131469,  0.33430929,  0.59000406])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0029657683204172736
Q = array([ 6.27838641, -0.53208338, -0.93904466])
E = 202.72706988176407
hkl_projection = array([ 0.7244245 , -0.42710291, -0.20756265])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
