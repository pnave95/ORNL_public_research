#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-377.597431843_hkl-24.9825349812,5.17606441873,-3.10605369711/sample/sampleassembly.xml'
psi = -0.005324303786111062
hkl2Q = array([[ -6.55696482e-01,   9.37847800e-01,   7.75090064e-17],
       [  6.63158539e-01,   4.63647429e-01,  -8.09165116e-01],
       [ -6.63158539e-01,  -4.63647429e-01,  -8.09165116e-01]])
pp = array([-0.91392123,  2.85740232,  0.24431516])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.001622429332826129
Q = array([ 21.87331764, -19.58983269,  -1.67498047])
E = -377.59743184305114
hkl_projection = array([-0.55711171, -0.00665515,  0.45265915])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
