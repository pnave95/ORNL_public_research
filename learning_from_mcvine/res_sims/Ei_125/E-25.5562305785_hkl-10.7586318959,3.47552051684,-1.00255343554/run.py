#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-25.5562305785_hkl-10.7586318959,3.47552051684,-1.00255343554/sample/sampleassembly.xml'
psi = -0.006062182091717243
hkl2Q = array([[ -6.55004286e-01,   9.38331368e-01,   7.74690622e-17],
       [  6.63500474e-01,   4.63157972e-01,  -8.09165116e-01],
       [ -6.63500474e-01,  -4.63157972e-01,  -8.09165116e-01]])
pp = array([-0.79811737,  2.8918867 ,  0.72144379])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0033563800897558112
Q = array([ 10.01815419,  -8.02110614,  -2.0010387 ])
E = -25.556230578518608
hkl_projection = array([ 0.41868226, -0.31815507,  0.95330616])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
