#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-17.0557325219_hkl-1.39707533481,-1.26424023571,0.712932865338/sample/sampleassembly.xml'
psi = 0.000635936292359975
hkl2Q = array([[-0.6612746 ,  0.93392306,  0.        ],
       [ 0.66038333,  0.46759175, -0.80916512],
       [-0.66038333, -0.46759175, -0.80916512]])
pp = array([ 2.64999651,  1.40624269, -0.2814028 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0066900314392080752
Q = array([-0.38184171, -2.2292707 ,  0.44609869])
E = -17.055732521897546
hkl_projection = array([ 0.95231028, -0.39179386, -0.10788104])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
