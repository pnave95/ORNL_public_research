#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-171.005230807_hkl-20.8466854012,2.58179585851,-0.736216435314/sample/sampleassembly.xml'
psi = -0.004205879059790656
hkl2Q = array([[-0.65674498,  0.93711387,  0.        ],
       [ 0.66263957,  0.46438883, -0.80916512],
       [-0.66263957, -0.46438883, -0.80916512]])
pp = array([-0.04700147,  2.99963179,  0.24893681])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016555162101338891
Q = array([ 15.8896023 , -17.9948701 ,  -1.49337849])
E = -171.00523080701907
hkl_projection = array([ 0.64158101, -0.76582492,  0.83403004])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
