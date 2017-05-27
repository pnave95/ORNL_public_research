#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-716.939863377_hkl-35.4866466825,5.17684578021,-12.6182469643/sample/sampleassembly.xml'
psi = -0.007650248925087437
hkl2Q = array([[ -6.53513328e-01,   9.39370375e-01,   7.73833762e-17],
       [  6.64235162e-01,   4.62103706e-01,  -8.09165116e-01],
       [ -6.64235162e-01,  -4.62103706e-01,  -8.09165116e-01]])
pp = array([-1.37275183,  2.66749928, -0.63961134])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011516675580109795
Q = array([ 35.01112288, -25.11192631,   6.02132226])
E = -716.93986337662091
hkl_projection = array([ 0.9219824 ,  0.99880635,  0.49905131])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
