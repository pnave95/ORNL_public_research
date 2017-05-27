#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E46.9878790641_hkl-1.90352609847,0.913603719528,-1.77023931947/sample/sampleassembly.xml'
psi = -0.025589206926071664
hkl2Q = array([[ -6.36557756e-01,   9.50941951e-01,  -7.64417334e-17],
       [  6.72417502e-01,   4.50114306e-01,  -8.09165116e-01],
       [ -6.72417502e-01,  -4.50114306e-01,  -8.09165116e-01]])
pp = array([ 2.90913357,  0.73276316, -0.84357452])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0059537790666188608
Q = array([ 3.01636733, -0.60210667,  0.69315964])
E = 46.987879064108839
hkl_projection = array([-0.16776464,  0.84141715,  0.43527381])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
