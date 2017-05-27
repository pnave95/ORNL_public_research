#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-33.9706212894_hkl-8.24205521263,1.26748361379,-1.30522525604/sample/sampleassembly.xml'
psi = -0.005215269128201421
hkl2Q = array([[-0.65579874,  0.9377763 ,  0.        ],
       [ 0.66310798,  0.46371973, -0.80916512],
       [-0.66310798, -0.46371973, -0.80916512]])
pp = array([-0.75694854,  2.90293453, -0.01356346])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047262704177437201
Q = array([ 7.11111317, -6.53618817,  0.03053922])
E = -33.97062128939541
hkl_projection = array([-0.06905678, -0.54321375, -0.44568505])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
