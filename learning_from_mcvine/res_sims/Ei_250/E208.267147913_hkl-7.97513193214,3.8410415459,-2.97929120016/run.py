#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E208.267147913_hkl-7.97513193214,3.8410415459,-2.97929120016/sample/sampleassembly.xml'
psi = -0.008110083049824263
hkl2Q = array([[ -6.53081304e-01,   9.39670784e-01,   7.73586371e-17],
       [  6.64447583e-01,   4.61798219e-01,  -8.09165116e-01],
       [ -6.64447583e-01,  -4.61798219e-01,  -8.09165116e-01]])
pp = array([ 0.84984796,  2.87710939,  0.46179273])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0030197014455173774
Q = array([ 9.74016317, -4.34438096, -0.69729832])
E = 208.26714791306136
hkl_projection = array([-0.77996378,  0.55116576,  0.58663308])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
