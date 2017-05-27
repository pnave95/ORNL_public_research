#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-76.3723089682_hkl-5.86138902341,-1.52089142783,2.47279123879/sample/sampleassembly.xml'
psi = -0.000808667701341398
hkl2Q = array([[ -6.59924762e-01,   9.34877361e-01,  -7.77552801e-17],
       [  6.61058122e-01,   4.66637274e-01,  -8.09165116e-01],
       [ -6.61058122e-01,  -4.66637274e-01,  -8.09165116e-01]])
pp = array([ 2.00141973,  2.23479732,  0.23441013])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032671163639231126
Q = array([ 1.22801939, -7.3432811 , -0.77024412])
E = -76.372308968210262
hkl_projection = array([ 0.93536098,  0.09286865,  0.51214572])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
