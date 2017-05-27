#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-59.6336880082_hkl0.306854088999,-2.32635938178,-0.57355170975/sample/sampleassembly.xml'
psi = 0.01211751639271578
hkl2Q = array([[ -6.71953691e-01,   9.26269188e-01,  -7.84778896e-17],
       [  6.54971224e-01,   4.75143011e-01,  -8.09165116e-01],
       [ -6.54971224e-01,  -4.75143011e-01,  -8.09165116e-01]])
pp = array([ 2.99463243,  0.17937846, -0.76724223])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0033030741622113689
Q = array([-1.35423032, -0.54860483,  2.3465069 ])
E = -59.633688008176065
hkl_projection = array([-0.54220415,  0.16846271, -0.95101733])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
