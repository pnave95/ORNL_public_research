#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E106.001875394_hkl-4.23776239162,2.66598537403,-1.60983860552/sample/sampleassembly.xml'
psi = -0.013533454764555487
hkl2Q = array([[-0.64797554,  0.94319885,  0.        ],
       [ 0.6669423 ,  0.4581879 , -0.80916512],
       [-0.6669423 , -0.4581879 , -0.80916512]])
pp = array([ 2.20395368,  2.03533491,  0.85351231])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0043699979903484946
Q = array([ 5.59769427, -2.03792181, -0.85459712])
E = 106.0018753938445
hkl_projection = array([ 0.13737746, -0.27671925,  0.20673542])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
