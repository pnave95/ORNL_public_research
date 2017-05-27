#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E10.9416790732_hkl-4.26272744663,1.7227527072,-0.696926381259/sample/sampleassembly.xml'
psi = -0.005699778165673948
hkl2Q = array([[ -6.55344298e-01,   9.38093931e-01,  -7.74886701e-17],
       [  6.63332580e-01,   4.63398397e-01,  -8.09165116e-01],
       [ -6.63332580e-01,  -4.63398397e-01,  -8.09165116e-01]])
pp = array([-0.59226111,  2.94095678,  0.84834937])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0073113914780755102
Q = array([ 4.3986061 , -2.87756333, -0.83006288])
E = 10.941679073209087
hkl_projection = array([ 0.74573515,  0.64533378, -0.25489975])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
