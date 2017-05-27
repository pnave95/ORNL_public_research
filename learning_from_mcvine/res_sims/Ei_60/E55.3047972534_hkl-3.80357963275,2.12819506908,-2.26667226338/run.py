#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E55.3047972534_hkl-3.80357963275,2.12819506908,-2.26667226338/sample/sampleassembly.xml'
psi = -0.01666999987874572
hkl2Q = array([[-0.64501397,  0.94522661,  0.        ],
       [ 0.66837615,  0.45609375, -0.80916512],
       [-0.66837615, -0.45609375, -0.80916512]])
pp = array([ 0.03016641,  2.99984833, -0.21130338])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0070159740953370416
Q = array([ 5.3907865 , -1.59077315,  0.11205092])
E = 55.30479725343946
hkl_projection = array([-0.53129966, -0.60565463, -0.08595347])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
