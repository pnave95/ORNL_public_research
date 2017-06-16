#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/notebooks/8-4dcovmat/out.res_comps_tmp/sample/sampleassembly.xml'
psi = 0.16641482070853725
hkl2Q = array([[-0.80632514,  0.81199516,  0.        ],
       [ 0.57416729,  0.57015797, -0.80916512],
       [-0.57416729, -0.57015797, -0.80916512]])
pp = array([ 2.23314751,  2.00326039,  0.        ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.003643048313977743
Q = array([ 3.67684263, -3.70269794,  0.        ])
E = 62.5
hkl_projection = array([ 1.,  0.,  0.])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
