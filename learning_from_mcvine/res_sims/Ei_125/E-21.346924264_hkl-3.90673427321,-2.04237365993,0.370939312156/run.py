#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-21.346924264_hkl-3.90673427321,-2.04237365993,0.370939312156/sample/sampleassembly.xml'
psi = -0.0009936755210688518
hkl2Q = array([[-0.65975179,  0.93499944,  0.        ],
       [ 0.66114444,  0.46651497, -0.80916512],
       [-0.66114444, -0.46651497, -0.80916512]])
pp = array([ 2.45720919,  1.72108193, -0.48710615])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0033557872425538111
Q = array([ 0.98192648, -4.77864096,  1.35246637])
E = -21.346924263983283
hkl_projection = array([-0.2462842 , -0.66673049,  0.88928498])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
