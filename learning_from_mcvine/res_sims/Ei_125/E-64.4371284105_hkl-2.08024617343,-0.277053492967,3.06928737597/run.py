#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-64.4371284105_hkl-2.08024617343,-0.277053492967,3.06928737597/sample/sampleassembly.xml'
psi = 0.001147613893547001
hkl2Q = array([[ -6.61752381e-01,   9.33584574e-01,  -7.78629522e-17],
       [  6.60143983e-01,   4.67929596e-01,  -8.09165116e-01],
       [ -6.60143983e-01,  -4.67929596e-01,  -8.09165116e-01]])
pp = array([ 2.7794902 ,  1.12890843,  0.72710276])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032948840794213884
Q = array([-0.83245893, -3.50793767, -2.25937826])
E = -64.437128410456324
hkl_projection = array([ 0.99105862, -0.27578529,  0.34446426])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
