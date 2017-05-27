#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E23.2957714043_hkl-1.34907075836,1.11685564214,-0.694784305125/sample/sampleassembly.xml'
psi = -0.017847936153745244
hkl2Q = array([[-0.64390011,  0.94598574,  0.        ],
       [ 0.66891293,  0.45530613, -0.80916512],
       [-0.66891293, -0.45530613, -0.80916512]])
pp = array([ 2.90374758,  0.75382359,  0.57039853])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.008340770326457787
Q = array([ 2.0804962 , -0.45135092, -0.3415254 ])
E = 23.295771404305043
hkl_projection = array([-0.87536765,  0.94026621,  0.65355182])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
