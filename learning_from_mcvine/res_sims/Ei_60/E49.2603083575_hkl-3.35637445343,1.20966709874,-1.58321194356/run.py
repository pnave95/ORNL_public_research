#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E49.2603083575_hkl-3.35637445343,1.20966709874,-1.58321194356/sample/sampleassembly.xml'
psi = -0.010433570913833913
hkl2Q = array([[-0.65089623,  0.94118567,  0.        ],
       [ 0.66551877,  0.46025314, -0.80916512],
       [-0.66551877, -0.46025314, -0.80916512]])
pp = array([ 1.76522945,  2.42568856, -0.39133791])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.006077201834533837
Q = array([ 4.04336491, -1.8735402 ,  0.30225946])
E = 49.26030835749475
hkl_projection = array([ 0.59422   , -0.34144246,  0.5149469 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
