#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E58.8718214202_hkl-6.98245478435,0.459077641315,-2.18222430415/sample/sampleassembly.xml'
psi = -0.005763764607855922
hkl2Q = array([[-0.65528427,  0.93813586,  0.        ],
       [ 0.66336223,  0.46335595, -0.80916512],
       [-0.66336223, -0.46335595, -0.80916512]])
pp = array([ 0.80151941,  2.89094563, -0.75674042])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0036457601112231206
Q = array([ 6.32763274, -5.32662826,  1.39431017])
E = 58.871821420235307
hkl_projection = array([ 0.73620533,  0.21318447,  0.98302724])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
