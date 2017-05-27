#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E47.0329201765_hkl-4.48672501647,1.62512733706,-2.04268501938/sample/sampleassembly.xml'
psi = -0.01022682524287869
hkl2Q = array([[-0.6510908 ,  0.94105108,  0.        ],
       [ 0.6654236 ,  0.46039072, -0.80916512],
       [-0.6654236 , -0.46039072, -0.80916512]])
pp = array([ 0.05312018,  2.99952967, -0.40000638])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0059012020634047167
Q = array([ 5.3619143 , -2.53361066,  0.33787311])
E = 47.032920176509435
hkl_projection = array([-0.16701191, -0.10413474, -0.48616347])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
