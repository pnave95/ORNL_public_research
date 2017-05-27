#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-130.636132909_hkl-21.7839744593,7.47963495921,-1.69122636028/sample/sampleassembly.xml'
psi = -0.0059992059634872506
hkl2Q = array([[ -6.55063377e-01,   9.38290117e-01,   7.74724681e-17],
       [  6.63471304e-01,   4.63199756e-01,  -8.09165116e-01],
       [ -6.63471304e-01,  -4.63199756e-01,  -8.09165116e-01]])
pp = array([-0.84397356,  2.87883807,  0.83275999])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016731504642759879
Q = array([ 20.3544872 , -16.19174722,  -4.68377832])
E = -130.6361329093445
hkl_projection = array([ 0.47261876,  0.39858898,  0.09209266])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
