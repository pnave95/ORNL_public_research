#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E159.450421986_hkl-2.8261363577,1.10350376255,-3.03225286012/sample/sampleassembly.xml'
psi = -0.021665689860416934
hkl2Q = array([[-0.64028388,  0.94843709,  0.        ],
       [ 0.6706463 ,  0.45274908, -0.80916512],
       [-0.6706463 , -0.45274908, -0.80916512]])
pp = array([ 2.97666721,  0.37343315, -0.7213398 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0027019503307700687
Q = array([ 4.58315944, -0.80795256,  1.56067649])
E = 159.45042198560634
hkl_projection = array([-0.42198614,  0.80002748, -0.66661528])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
