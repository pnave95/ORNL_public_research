#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E221.138677913_hkl-6.03407890662,2.89385252261,-3.70261187419/sample/sampleassembly.xml'
psi = -0.01144584133082878
hkl2Q = array([[-0.64994316,  0.94184407,  0.        ],
       [ 0.66598433,  0.45957922, -0.80916512],
       [-0.66598433, -0.45957922, -0.80916512]])
pp = array([ 2.14372016,  2.09868146, -0.51796565])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032249490361873495
Q = array([ 8.31495025, -2.65156351,  0.65441985])
E = 221.13867791283889
hkl_projection = array([-0.49181915,  0.90140906,  0.76936589])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
