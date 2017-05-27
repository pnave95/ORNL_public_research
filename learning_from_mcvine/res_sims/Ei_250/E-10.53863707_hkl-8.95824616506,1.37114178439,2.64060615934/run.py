#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-10.53863707_hkl-8.95824616506,1.37114178439,2.64060615934/sample/sampleassembly.xml'
psi = -0.0020230300394523037
hkl2Q = array([[-0.658789  ,  0.93567806,  0.        ],
       [ 0.6616243 ,  0.46583417, -0.80916512],
       [-0.6616243 , -0.46583417, -0.80916512]])
pp = array([ 1.66014048,  2.49878642,  0.90394744])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0024101390681235194
Q = array([ 5.06168551, -8.97339427, -3.24616649])
E = -10.538637069951022
hkl_projection = array([-0.00690894,  0.66766965, -0.11560939])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
