#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-6.08852047615_hkl-2.53890925769,-1.25819155014,-0.241229555574/sample/sampleassembly.xml'
psi = -0.0013059199096375647
hkl2Q = array([[ -6.59459810e-01,   9.35205395e-01,   7.77280066e-17],
       [  6.61290076e-01,   4.66308504e-01,  -8.09165116e-01],
       [ -6.61290076e-01,  -4.66308504e-01,  -8.09165116e-01]])
pp = array([ 2.10956569,  2.13301022, -0.9084881 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0068774120093775346
Q = array([ 1.00180174, -2.84861966,  1.21327925])
E = -6.0885204761466838
hkl_projection = array([ 0.15015458,  0.93994397,  0.67084582])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
