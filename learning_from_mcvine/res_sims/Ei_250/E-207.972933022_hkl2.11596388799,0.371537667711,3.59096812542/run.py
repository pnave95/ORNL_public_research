#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-207.972933022_hkl2.11596388799,0.371537667711,3.59096812542/sample/sampleassembly.xml'
psi = -0.024400470217522428
hkl2Q = array([[ -6.37687726e-01,   9.50184580e-01,  -7.65026634e-17],
       [  6.71881960e-01,   4.50913315e-01,  -8.09165116e-01],
       [ -6.71881960e-01,  -4.50913315e-01,  -8.09165116e-01]])
pp = array([ 2.99778509, -0.11525864,  0.6612536 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0022954165679195272
Q = array([-3.51240144,  0.5588722 , -3.20632146])
E = -207.97293302186972
hkl_projection = array([ 0.83860045, -0.07534206,  0.86851517])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
