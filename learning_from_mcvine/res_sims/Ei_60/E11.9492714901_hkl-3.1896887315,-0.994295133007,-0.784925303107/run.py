#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E11.9492714901_hkl-3.1896887315,-0.994295133007,-0.784925303107/sample/sampleassembly.xml'
psi = -0.0030402571747734602
hkl2Q = array([[-0.65783686,  0.93634771,  0.        ],
       [ 0.66209782,  0.4651609 , -0.80916512],
       [-0.66209782, -0.4651609 , -0.80916512]])
pp = array([ 2.23579146,  2.00030911, -0.93377628])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0050510142937559357
Q = array([ 1.9596715 , -3.08404841,  1.43968311])
E = 11.949271490116558
hkl_projection = array([ 0.8555148 ,  0.61211634,  0.10368806])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
