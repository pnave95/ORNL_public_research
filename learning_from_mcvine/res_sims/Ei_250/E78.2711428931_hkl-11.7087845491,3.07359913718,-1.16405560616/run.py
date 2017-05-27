#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E78.2711428931_hkl-11.7087845491,3.07359913718,-1.16405560616/sample/sampleassembly.xml'
psi = -0.004189159745004764
hkl2Q = array([[ -6.56760652e-01,   9.37102885e-01,  -7.75706192e-17],
       [  6.62631805e-01,   4.64399910e-01,  -8.09165116e-01],
       [ -6.62631805e-01,  -4.64399910e-01,  -8.09165116e-01]])
pp = array([ 0.17479878,  2.99490323,  0.51392082])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0024961262667033755
Q = array([ 10.49787378,  -9.0043693 ,  -1.54513601])
E = 78.271142893060812
hkl_projection = array([-0.17863852, -0.09735597,  0.49697816])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
