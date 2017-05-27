#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E16.4102945298_hkl-1.84851110625,-0.351059640732,-0.283121426921/sample/sampleassembly.xml'
psi = -0.0031784148643042654
hkl2Q = array([[ -6.57707488e-01,   9.36438589e-01,  -7.76256467e-17],
       [  6.62162077e-01,   4.65069425e-01,  -8.09165116e-01],
       [ -6.62162077e-01,  -4.65069425e-01,  -8.09165116e-01]])
pp = array([ 2.76978356,  1.15251856, -0.33553772])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0050593856536502628
Q = array([ 1.17079349, -1.76261312,  0.5131572 ])
E = 16.410294529761401
hkl_projection = array([ 0.02039174,  0.33632811, -0.84394438])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
