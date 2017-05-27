#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E16.3562698154_hkl-3.09263090175,0.508850757422,-0.6305698199/sample/sampleassembly.xml'
psi = -0.004375907607990011
hkl2Q = array([[-0.65658564,  0.93722552,  0.        ],
       [ 0.66271852,  0.46427616, -0.80916512],
       [-0.66271852, -0.46427616, -0.80916512]])
pp = array([ 1.19930824,  2.74984722, -0.114301  ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0075313554838101265
Q = array([ 2.78569215, -2.36948679,  0.09849082])
E = 16.356269815369622
hkl_projection = array([ 0.55468901,  0.73687559,  0.82628481])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
