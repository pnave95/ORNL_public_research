#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E16.7230734859_hkl-0.6431854897,0.300455910119,-1.11884628553/sample/sampleassembly.xml'
psi = 0.05177714258312896
hkl2Q = array([[ -7.08151167e-01,   8.98898379e-01,  -8.08674849e-17],
       [  6.35617139e-01,   5.00738492e-01,  -8.09165116e-01],
       [ -6.35617139e-01,  -5.00738492e-01,  -8.09165116e-01]])
pp = array([ 2.99566044, -0.16130262, -0.80591519])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0076210580414190904
Q = array([ 1.35760536,  0.13254085,  0.66221294])
E = 16.723073485867403
hkl_projection = array([-0.83981513, -0.89149482, -0.71924377])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
