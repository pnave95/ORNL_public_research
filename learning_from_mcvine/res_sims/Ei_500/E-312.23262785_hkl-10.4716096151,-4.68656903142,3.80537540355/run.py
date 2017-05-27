#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-312.23262785_hkl-10.4716096151,-4.68656903142,3.80537540355/sample/sampleassembly.xml'
psi = -0.000450044166947185
hkl2Q = array([[-0.66025999,  0.93464064,  0.        ],
       [ 0.66089073,  0.46687432, -0.80916512],
       [-0.66089073, -0.46687432, -0.80916512]])
pp = array([ 2.16278712,  2.07902667, -0.10779709])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016308787907496677
Q = array([  1.30173747, -13.75186262,   0.71303114])
E = -312.23262785013748
hkl_projection = array([-0.18788468,  0.68309732, -0.08131513])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
