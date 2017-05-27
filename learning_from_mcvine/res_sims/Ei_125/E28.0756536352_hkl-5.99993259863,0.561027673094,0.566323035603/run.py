#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E28.0756536352_hkl-5.99993259863,0.561027673094,0.566323035603/sample/sampleassembly.xml'
psi = -0.0033940742308353066
hkl2Q = array([[ -6.57505521e-01,   9.36580408e-01,  -7.76138925e-17],
       [  6.62262358e-01,   4.64926612e-01,  -8.09165116e-01],
       [ -6.62262358e-01,  -4.64926612e-01,  -8.09165116e-01]])
pp = array([ 1.69896639,  2.47255197,  0.4011991 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0034822873973587949
Q = array([ 3.94148189, -5.62188128, -0.91221287])
E = 28.075653635195636
hkl_projection = array([-0.90587794, -0.37651318, -0.39284386])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
