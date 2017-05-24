#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-89.2532713689_hkl-8.04143747444,-0.85570610914,4.06029027011/sample/sampleassembly.xml'
psi = -0.0009958846736223877
hkl2Q = array([[-0.65974973,  0.93500089,  0.        ],
       [ 0.66114547,  0.4665135 , -0.80916512],
       [-0.66114547, -0.4665135 , -0.80916512]])
pp = array([ 2.42997486,  1.75932436,  0.46493416])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016755397326101997
Q = array([ 2.05514742, -9.81212993, -2.59303772])
E = -89.253271368922469
hkl_projection = array([-0.48856925, -0.68454576, -0.36215096])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
