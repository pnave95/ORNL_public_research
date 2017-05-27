#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-3.31006801043_hkl-7.12479766726,-1.54526457364,-1.2440741629/sample/sampleassembly.xml'
psi = -0.003187976888412938
hkl2Q = array([[-0.65769853,  0.93644488,  0.        ],
       [ 0.66216652,  0.46506309, -0.80916512],
       [-0.66216652, -0.46506309, -0.80916512]])
pp = array([ 1.31366059,  2.69709026, -0.89362618])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0034125955716977577
Q = array([ 4.48653077, -6.81205283,  2.2570356 ])
E = -3.3100680104294753
hkl_projection = array([ 0.82754205,  0.00966346, -0.82508523])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
