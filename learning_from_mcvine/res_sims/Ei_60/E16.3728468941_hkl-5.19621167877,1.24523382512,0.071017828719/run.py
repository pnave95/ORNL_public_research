#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E16.3728468941_hkl-5.19621167877,1.24523382512,0.071017828719/sample/sampleassembly.xml'
psi = -0.004638869907003333
hkl2Q = array([[ -6.56339160e-01,   9.37398143e-01,   7.75461864e-17],
       [  6.62840583e-01,   4.64101871e-01,  -8.09165116e-01],
       [ -6.62840583e-01,  -4.64101871e-01,  -8.09165116e-01]])
pp = array([ 0.8130476 ,  2.88772464,  0.71096632])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0050810876358123678
Q = array([ 4.18879523, -4.32596334, -1.06506492])
E = 16.372846894146832
hkl_projection = array([-0.0304762 , -0.40933369, -0.68617738])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
