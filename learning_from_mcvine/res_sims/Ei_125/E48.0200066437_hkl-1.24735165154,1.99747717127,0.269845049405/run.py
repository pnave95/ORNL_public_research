#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E48.0200066437_hkl-1.24735165154,1.99747717127,0.269845049405/sample/sampleassembly.xml'
psi = -0.02472011227963566
hkl2Q = array([[-0.63738397,  0.95038836,  0.        ],
       [ 0.67202606,  0.45069853, -0.80916512],
       [-0.67202606, -0.45069853, -0.80916512]])
pp = array([ 2.99276788,  0.20818358,  0.93882977])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0035965085752254085
Q = array([ 1.95605575, -0.40682724, -1.83463805])
E = 48.020006643728465
hkl_projection = array([-0.18455771, -0.48188809,  0.07438323])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
