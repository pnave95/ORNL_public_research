#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-756.651782701_hkl-7.62685386334,-1.27881685617,10.8848809162/sample/sampleassembly.xml'
psi = 0.0012700979093998135
hkl2Q = array([[-0.66186673,  0.93350351,  0.        ],
       [ 0.66008666,  0.46801045, -0.80916512],
       [-0.66008666, -0.46801045, -0.80916512]])
pp = array([ 2.67133324,  1.36527605,  0.8282692 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011521985006555967
Q = array([ -2.9811339 , -12.81243254,  -7.77289194])
E = -756.65178270120032
hkl_projection = array([-0.35068235, -0.41918857,  0.48981988])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
