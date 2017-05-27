#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-19.6538025864_hkl-5.61066528124,0.416964459049,1.24607278309/sample/sampleassembly.xml'
psi = -0.0026675583954172835
hkl2Q = array([[ -6.58185788e-01,   9.36102473e-01,  -7.76535189e-17],
       [  6.61924407e-01,   4.65407634e-01,  -8.09165116e-01],
       [ -6.61924407e-01,  -4.65407634e-01,  -8.09165116e-01]])
pp = array([ 1.11737163,  2.7841481 ,  0.6645138 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.004805179743207281
Q = array([ 3.14405311, -5.63803099, -1.34567172])
E = -19.653802586400758
hkl_projection = array([-0.90074232,  0.01721536,  0.81186138])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
