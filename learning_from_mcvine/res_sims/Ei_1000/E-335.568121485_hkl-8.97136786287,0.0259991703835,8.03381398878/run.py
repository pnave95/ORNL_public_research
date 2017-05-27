#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-335.568121485_hkl-8.97136786287,0.0259991703835,8.03381398878/sample/sampleassembly.xml'
psi = -0.00028503615169075703
hkl2Q = array([[-0.6604142 ,  0.93453168,  0.        ],
       [ 0.66081368,  0.46698336, -0.80916512],
       [-0.66081368, -0.46698336, -0.80916512]])
pp = array([ 2.61185062,  1.47588494,  0.79393518])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.001176305667519224
Q = array([  0.63314513, -12.12354372,  -6.52171965])
E = -335.56812148488007
hkl_projection = array([ 0.61479668, -0.62955938, -0.25013695])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
