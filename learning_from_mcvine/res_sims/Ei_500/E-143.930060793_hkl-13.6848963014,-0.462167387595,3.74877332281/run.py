#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-143.930060793_hkl-13.6848963014,-0.462167387595,3.74877332281/sample/sampleassembly.xml'
psi = -0.002006613516577162
hkl2Q = array([[-0.65880436,  0.93566724,  0.        ],
       [ 0.66161665,  0.46584503, -0.80916512],
       [-0.66161665, -0.46584503, -0.80916512]])
pp = array([ 1.60834976,  2.53243184,  0.45609481])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016631537125239156
Q = array([  6.2296408 , -14.766155  ,  -2.65940687])
E = -143.93006079261914
hkl_projection = array([ 0.50595549,  0.48260881, -0.38906981])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
