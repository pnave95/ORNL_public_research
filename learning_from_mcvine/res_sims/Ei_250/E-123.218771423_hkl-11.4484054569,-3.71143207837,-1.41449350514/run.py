#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-123.218771423_hkl-11.4484054569,-3.71143207837,-1.41449350514/sample/sampleassembly.xml'
psi = -0.0018338781965478203
hkl2Q = array([[-0.65896597,  0.93555343,  0.        ],
       [ 0.66153618,  0.46595931, -0.80916512],
       [-0.66153618, -0.46595931, -0.80916512]])
pp = array([ 1.17182218,  2.7616721 , -0.97230835])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023401824958029825
Q = array([  6.02460164, -11.78087491,   4.14772017])
E = -123.21877142316119
hkl_projection = array([-0.06911419, -0.88288086, -0.48304808])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
