#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-222.376905428_hkl-23.9769496891,5.87483843373,-6.46552150407/sample/sampleassembly.xml'
psi = -0.00679077858058449
hkl2Q = array([[-0.65432045,  0.93880835,  0.        ],
       [ 0.66383775,  0.46267443, -0.80916512],
       [-0.66383775, -0.46267443, -0.80916512]])
pp = array([-1.32532316,  2.69137855, -0.07656887])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016452013820930861
Q = array([ 23.88060525, -16.80019171,   0.47796014])
E = -222.37690542829071
hkl_projection = array([-0.62286118, -0.94514866, -0.59197215])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
