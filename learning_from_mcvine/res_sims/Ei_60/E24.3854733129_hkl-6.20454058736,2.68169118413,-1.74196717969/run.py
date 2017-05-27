#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E24.3854733129_hkl-6.20454058736,2.68169118413,-1.74196717969/sample/sampleassembly.xml'
psi = -0.008880242596980172
hkl2Q = array([[ -6.52357414e-01,   9.40173482e-01,  -7.73172744e-17],
       [  6.64803044e-01,   4.61286351e-01,  -8.09165116e-01],
       [ -6.64803044e-01,  -4.61286351e-01,  -8.09165116e-01]])
pp = array([-1.1546765 ,  2.76888464,  0.55511847])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.005180368328393024
Q = array([ 6.9884396 , -3.7927713 , -0.76039188])
E = 24.385473312904011
hkl_projection = array([ 0.05443248,  0.68051602, -0.52047954])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
