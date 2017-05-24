#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E33.9663105369_hkl-7.95667758146,1.23072947792,-0.753415673231/sample/sampleassembly.xml'
psi = -0.004844876805951646
hkl2Q = array([[ -6.56146036e-01,   9.37533333e-01,  -7.75350044e-17],
       [  6.62936177e-01,   4.63965312e-01,  -8.09165116e-01],
       [ -6.62936177e-01,  -4.63965312e-01,  -8.09165116e-01]])
pp = array([ 0.57124541,  2.94511098,  0.1739508 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0034990876026114726
Q = array([ 6.53610406, -6.53907593, -0.38622568])
E = 33.966310536859567
hkl_projection = array([ 0.93541926,  0.48345558,  0.00880027])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
