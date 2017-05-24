#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E99.7916898185_hkl-4.15610257518,1.89196700781,-1.65447443521/sample/sampleassembly.xml'
psi = -0.010864177852001024
hkl2Q = array([[-0.65049089,  0.94146587,  0.        ],
       [ 0.6657169 ,  0.45996652, -0.80916512],
       [-0.6657169 , -0.45996652, -0.80916512]])
pp = array([ 2.305393  ,  1.91967787,  0.16168845])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0041200839783712435
Q = array([ 5.06443285, -2.28158439, -0.19217071])
E = 99.791689818466438
hkl_projection = array([ 0.90940385,  0.28782534, -0.16218324])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
