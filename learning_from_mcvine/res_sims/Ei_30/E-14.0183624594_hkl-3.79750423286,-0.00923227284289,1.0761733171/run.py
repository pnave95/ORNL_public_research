#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-14.0183624594_hkl-3.79750423286,-0.00923227284289,1.0761733171/sample/sampleassembly.xml'
psi = -0.001633742196938378
hkl2Q = array([[-0.65915319,  0.93542153,  0.        ],
       [ 0.66144291,  0.46609169, -0.80916512],
       [-0.66144291, -0.46609169, -0.80916512]])
pp = array([ 1.34419138,  2.68200476,  0.5705679 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0067378100971739897
Q = array([ 1.78520321, -4.05816575, -0.86333147])
E = -14.018362459428257
hkl_projection = array([ 0.01220172, -0.16535796, -0.23263778])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
