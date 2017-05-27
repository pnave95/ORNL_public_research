#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-12.6319588353_hkl-15.1343043625,3.38090749305,-5.21990640685/sample/sampleassembly.xml'
psi = -0.005509425954225761
hkl2Q = array([[ -6.55522854e-01,   9.37969167e-01,  -7.74989772e-17],
       [  6.63244359e-01,   4.63524655e-01,  -8.09165116e-01],
       [ -6.63244359e-01,  -4.63524655e-01,  -8.09165116e-01]])
pp = array([-1.23286191,  2.73496828, -0.39865325])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023933612389734323
Q = array([ 15.62532369, -10.20882156,   1.48805377])
E = -12.631958835306506
hkl_projection = array([-0.71611969,  0.57092725,  0.55530504])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
