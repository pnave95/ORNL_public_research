#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E13.3885343925_hkl-4.44755809092,-2.5302797192,-0.976216862561/sample/sampleassembly.xml'
psi = -0.001398294692033793
hkl2Q = array([[-0.65937342,  0.93526631,  0.        ],
       [ 0.66133315,  0.46624742, -0.80916512],
       [-0.66133315, -0.46624742, -0.80916512]])
pp = array([ 2.64452668,  1.41650226, -0.82287112])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0024284824478646608
Q = array([ 1.9048483 , -4.88422903,  2.83733471])
E = 13.388534392493511
hkl_projection = array([-0.24035908, -0.30085766, -0.4811223 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
