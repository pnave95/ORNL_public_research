#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-28.2693003992_hkl-1.39155212315,-1.03095269565,1.61422751369/sample/sampleassembly.xml'
psi = 0.0012078015703042408
hkl2Q = array([[-0.66180857,  0.93354474,  0.        ],
       [ 0.66011582,  0.46796933, -0.80916512],
       [-0.66011582, -0.46796933, -0.80916512]])
pp = array([ 2.63280752,  1.43816709,  0.26755288])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0065885136814939895
Q = array([-0.82518418, -2.53693937, -0.47196564])
E = -28.269300399168095
hkl_projection = array([-0.35294102,  0.86713486,  0.63231956])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
