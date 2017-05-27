#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-18.7223657245_hkl0.377051893672,-0.781385774485,0.40077192738/sample/sampleassembly.xml'
psi = 0.01820149718721794
hkl2Q = array([[ -6.77576624e-01,   9.22163917e-01,   7.88272559e-17],
       [  6.52068359e-01,   4.79119025e-01,  -8.09165116e-01],
       [ -6.52068359e-01,  -4.79119025e-01,  -8.09165116e-01]])
pp = array([ 2.99694914,  0.13526213, -0.19048809])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0066704970316402053
Q = array([-1.02632918, -0.21869059,  0.30797945])
E = -18.7223657244793
hkl_projection = array([ 0.1545391 ,  0.23671958,  0.05577768])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
