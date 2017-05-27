#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-26.4907105033_hkl-2.46613302561,-1.80811708075,0.653882494672/sample/sampleassembly.xml'
psi = -2.9241030834433713e-06
hkl2Q = array([[ -6.60677819e-01,   9.34345328e-01,   7.77995554e-17],
       [  6.60681917e-01,   4.67169766e-01,  -8.09165116e-01],
       [ -6.60681917e-01,  -4.67169766e-01,  -8.09165116e-01]])
pp = array([ 2.224182  ,  2.01320999, -0.54431304])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0066137775117296634
Q = array([  2.72078915e-03,  -3.45439163e+00,   9.33966363e-01])
E = -26.490710503256189
hkl_projection = array([ 0.51784418, -0.80343705, -0.34909258])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
