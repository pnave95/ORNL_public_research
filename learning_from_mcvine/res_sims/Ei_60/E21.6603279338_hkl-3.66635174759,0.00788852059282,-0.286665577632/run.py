#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E21.6603279338_hkl-3.66635174759,0.00788852059282,-0.286665577632/sample/sampleassembly.xml'
psi = -0.003780559423730652
hkl2Q = array([[ -6.57143497e-01,   9.36834455e-01,   7.75928455e-17],
       [  6.62441996e-01,   4.64670623e-01,  -8.09165116e-01],
       [ -6.62441996e-01,  -4.64670623e-01,  -8.09165116e-01]])
pp = array([ 1.94259478,  2.28611582, -0.15637082])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0051218604355857192
Q = array([ 2.60444421, -3.297894  ,  0.22557667])
E = 21.660327933786306
hkl_projection = array([ 0.41944697,  0.4288528 , -0.71050593])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
