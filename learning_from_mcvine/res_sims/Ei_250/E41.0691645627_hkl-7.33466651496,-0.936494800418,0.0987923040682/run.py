#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E41.0691645627_hkl-7.33466651496,-0.936494800418,0.0987923040682/sample/sampleassembly.xml'
psi = -0.0020248746009475993
hkl2Q = array([[-0.65878727,  0.93567927,  0.        ],
       [ 0.66162516,  0.46583295, -0.80916512],
       [-0.66162516, -0.46583295, -0.80916512]])
pp = array([ 2.05028538,  2.19005248, -0.2021063 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.002441421773840336
Q = array([ 4.14701293, -7.34516629,  0.67783964])
E = 41.069164562735409
hkl_projection = array([-0.97306916,  0.92747155, -0.10932696])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
