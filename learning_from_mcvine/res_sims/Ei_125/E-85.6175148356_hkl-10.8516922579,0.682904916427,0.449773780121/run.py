#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-85.6175148356_hkl-10.8516922579,0.682904916427,0.449773780121/sample/sampleassembly.xml'
psi = -0.0035089907764315345
hkl2Q = array([[ -6.57397888e-01,   9.36655961e-01,  -7.76076320e-17],
       [  6.62315781e-01,   4.64850504e-01,  -8.09165116e-01],
       [ -6.62315781e-01,  -4.64850504e-01,  -8.09165116e-01]])
pp = array([ 0.15378522,  2.99605576,  0.27306843])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032569625071978978
Q = array([  7.288286  , -10.05593111,  -0.91652409])
E = -85.617514835554999
hkl_projection = array([ 0.35660826,  0.85835325,  0.67406624])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
