#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-60.0111445597_hkl0.663457919501,-2.33270797243,-1.071085784/sample/sampleassembly.xml'
psi = -0.07704103605870694
hkl2Q = array([[ -5.86809247e-01,   9.82421131e-01,  -7.39923530e-17],
       [  6.94676644e-01,   4.14936798e-01,  -8.09165116e-01],
       [ -6.94676644e-01,  -4.14936798e-01,  -8.09165116e-01]])
pp = array([ 2.99969991, -0.04243199, -0.91088117])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0033090278837001994
Q = array([-1.26574271,  0.12830161,  2.75423117])
E = -60.01114455973709
hkl_projection = array([ 0.23498565, -0.70918229, -0.03348376])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
