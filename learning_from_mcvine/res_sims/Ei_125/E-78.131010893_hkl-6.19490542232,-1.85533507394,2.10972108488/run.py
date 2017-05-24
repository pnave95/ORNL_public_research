#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-78.131010893_hkl-6.19490542232,-1.85533507394,2.10972108488/sample/sampleassembly.xml'
psi = -0.0009277595286183473
hkl2Q = array([[-0.65981342,  0.93495595,  0.        ],
       [ 0.66111369,  0.46655854, -0.80916512],
       [-0.66111369, -0.46655854, -0.80916512]])
pp = array([ 1.91521162,  2.30910468,  0.0621975 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032636724656188798
Q = array([ 1.46612883, -7.64189449, -0.20584029])
E = -78.131010893004117
hkl_projection = array([ 0.41646648,  0.22977   , -0.19684646])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
