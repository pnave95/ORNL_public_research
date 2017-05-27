#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E112.312131374_hkl-5.37022465303,1.16239567059,0.0737767316843/sample/sampleassembly.xml'
psi = -0.0033746584578336425
hkl2Q = array([[-0.65752371,  0.93656764,  0.        ],
       [ 0.66225333,  0.46493947, -0.80916512],
       [-0.66225333, -0.46493947, -0.80916512]])
pp = array([ 2.49459355,  1.66643422,  0.36849861])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0025529770197163918
Q = array([ 4.25199153, -4.52343673, -1.00026759])
E = 112.31213137412595
hkl_projection = array([-0.35537792, -0.22695533,  0.53642715])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
