#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-20.8356844174_hkl-7.24947895792,1.17719351431,-0.0949854005734/sample/sampleassembly.xml'
psi = -0.004326016419191012
hkl2Q = array([[ -6.56632397e-01,   9.37192759e-01,  -7.75631805e-17],
       [  6.62695355e-01,   4.64309220e-01,  -8.09165116e-01],
       [ -6.62695355e-01,  -4.64309220e-01,  -8.09165116e-01]])
pp = array([-0.09499256,  2.99849569,  0.42326889])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047885693945294797
Q = array([ 5.6033098 , -6.20347478, -0.87568505])
E = -20.835684417363865
hkl_projection = array([ 0.04634741, -0.39536309, -0.05694242])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
