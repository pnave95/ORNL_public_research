#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E230.02356361_hkl-5.84161225964,3.17094926535,-4.25675831187/sample/sampleassembly.xml'
psi = -0.015238347812589217
hkl2Q = array([[-0.64636655,  0.94430221,  0.        ],
       [ 0.66772249,  0.45705017, -0.80916512],
       [-0.66772249, -0.45705017, -0.80916512]])
pp = array([ 2.19987104,  2.0397469 , -0.84477644])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0034949776562949895
Q = array([ 8.73547017, -2.12141235,  0.8785988 ])
E = 230.02356361034413
hkl_projection = array([ 0.81050966, -0.69378886, -0.40002324])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
