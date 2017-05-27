#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E109.577714573_hkl-5.25864758896,2.88009745416,-2.24248299843/sample/sampleassembly.xml'
psi = -0.012870571724619076
hkl2Q = array([[ -6.48600629e-01,   9.42769111e-01,   7.71044048e-17],
       [  6.66638431e-01,   4.58629903e-01,  -8.09165116e-01],
       [ -6.66638431e-01,  -4.58629903e-01,  -8.09165116e-01]])
pp = array([ 1.05399085,  2.80875476,  0.5555817 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0044940613044455397
Q = array([ 6.82567113, -2.60832194, -0.51593538])
E = 109.57771457313427
hkl_projection = array([-0.96122323,  0.30293468,  0.93750495])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
