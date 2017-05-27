#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E862.137020372_hkl-8.48302567539,8.08356281861,-5.1637129087/sample/sampleassembly.xml'
psi = -0.03868492183364797
hkl2Q = array([[ -6.24050264e-01,   9.59196351e-01,   7.57839112e-17],
       [  6.78254244e-01,   4.41270174e-01,  -8.09165116e-01],
       [ -6.78254244e-01,  -4.41270174e-01,  -8.09165116e-01]])
pp = array([ 2.87864923,  0.84461743,  0.87093034])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.001568427896867973
Q = array([ 14.2788554 ,  -2.29125961,  -2.36264069])
E = 862.13702037233134
hkl_projection = array([ 0.55284752, -0.27141965,  0.89405575])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
