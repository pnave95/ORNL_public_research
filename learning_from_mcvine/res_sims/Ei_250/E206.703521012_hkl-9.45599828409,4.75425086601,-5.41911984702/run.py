#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E206.703521012_hkl-9.45599828409,4.75425086601,-5.41911984702/sample/sampleassembly.xml'
psi = -0.011148737888116485
hkl2Q = array([[-0.65022296,  0.94165093,  0.        ],
       [ 0.66584776,  0.45977706, -0.80916512],
       [-0.66584776, -0.45977706, -0.80916512]])
pp = array([-1.22945736,  2.73650043, -0.34830558])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0029961344545658746
Q = array([ 12.92242327,  -4.22676708,   0.53798879])
E = 206.70352101163803
hkl_projection = array([ 0.17072103,  0.64342376, -0.49561952])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
