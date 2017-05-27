#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-58.7077034746_hkl-9.41299006636,-1.66405386477,-1.39898476466/sample/sampleassembly.xml'
psi = -0.003257317084850718
hkl2Q = array([[-0.6576336 ,  0.93649048,  0.        ],
       [ 0.66219877,  0.46501718, -0.80916512],
       [-0.66219877, -0.46501718, -0.80916512]])
pp = array([ 0.58897861,  2.94161592, -0.81566907])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0033064496231453053
Q = array([ 6.0147701 , -8.93843728,  2.47850401])
E = -58.70770347456984
hkl_projection = array([-0.04419134, -0.3898039 ,  0.30748177])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
