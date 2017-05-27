#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-0.412323572114_hkl-0.114105984918,0.601784733872,0.572415327062/sample/sampleassembly.xml'
psi = -0.003767126290325647
hkl2Q = array([[-0.65715608,  0.93682563,  0.        ],
       [ 0.66243575,  0.46467952, -0.80916512],
       [-0.66243575, -0.46467952, -0.80916512]])
pp = array([ 2.99906026,  0.07508382,  0.76502666])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0069669907763523706
Q = array([ 0.09444079, -0.09325005, -0.95012173])
E = -0.41232357211364601
hkl_projection = array([ 0.78357803, -0.11130128, -0.66259963])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
