#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-372.198280638_hkl-2.04736776046,-5.98649383947,2.00232647941/sample/sampleassembly.xml'
psi = 0.0032865618765976633
hkl2Q = array([[ -6.63747755e-01,   9.32166986e-01,   7.79813619e-17],
       [  6.59141597e-01,   4.69340538e-01,  -8.09165116e-01],
       [ -6.59141597e-01,  -4.69340538e-01,  -8.09165116e-01]])
pp = array([ 2.88133598,  0.83540587, -0.47600545])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016252719573723094
Q = array([-3.90682803, -5.65796586,  3.22384925])
E = -372.19828063781574
hkl_projection = array([-0.38984351,  0.29852799,  0.71582668])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
