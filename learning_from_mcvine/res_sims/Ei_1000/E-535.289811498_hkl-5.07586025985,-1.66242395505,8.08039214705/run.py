#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-535.289811498_hkl-5.07586025985,-1.66242395505,8.08039214705/sample/sampleassembly.xml'
psi = 0.0018002986814362474
hkl2Q = array([[ -6.62361577e-01,   9.33152460e-01,   7.78990082e-17],
       [  6.59838432e-01,   4.68360362e-01,  -8.09165116e-01],
       [ -6.59838432e-01,  -4.68360362e-01,  -8.09165116e-01]])
pp = array([ 2.81385882,  1.04028772,  0.58092388])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011606222981875775
Q = array([-3.0666297 , -9.29970037, -5.19319598])
E = -535.28981149783976
hkl_projection = array([-0.56767304, -0.0404845 ,  0.47293802])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
