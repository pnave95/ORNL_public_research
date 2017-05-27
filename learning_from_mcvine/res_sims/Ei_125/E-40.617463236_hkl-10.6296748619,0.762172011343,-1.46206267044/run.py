#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-40.617463236_hkl-10.6296748619,0.762172011343,-1.46206267044/sample/sampleassembly.xml'
psi = -0.004585398950715904
hkl2Q = array([[-0.65638928,  0.93736305,  0.        ],
       [ 0.66281577,  0.46413731, -0.80916512],
       [-0.66281577, -0.46413731, -0.80916512]])
pp = array([-0.21675685,  2.99215917, -0.18972604])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0033158426830660784
Q = array([ 8.45146248, -8.9315141 ,  0.56632711])
E = -40.617463236021081
hkl_projection = array([-0.11478921,  0.50904659, -0.3172941 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
