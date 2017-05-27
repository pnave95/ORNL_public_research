#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E457.069253233_hkl-10.2096578842,5.0193663129,-6.33635219839/sample/sampleassembly.xml'
psi = -0.015517437827149613
hkl2Q = array([[-0.64610298,  0.94448257,  0.        ],
       [ 0.66785003,  0.4568638 , -0.80916512],
       [-0.66785003, -0.4568638 , -0.80916512]])
pp = array([ 0.91530871,  2.85695817, -0.68342567])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.002409339607521409
Q = array([ 14.18040725,  -4.45482721,   1.06565904])
E = 457.06925323262192
hkl_projection = array([ 0.4681278 , -0.88002788, -0.69600383])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
