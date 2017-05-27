#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E0.985220570461_hkl-5.68456730538,-0.440034442761,-0.989638400087/sample/sampleassembly.xml'
psi = -0.003870427661159343
hkl2Q = array([[-0.6570593 ,  0.93689351,  0.        ],
       [ 0.66248375,  0.46461109, -0.80916512],
       [-0.66248375, -0.46461109, -0.80916512]])
pp = array([ 0.74913463,  2.90496081, -0.66277305])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0049308113707249622
Q = array([ 4.09920152, -5.07048211,  1.15684139])
E = 0.98522057046106681
hkl_projection = array([-0.79986673,  0.35072998,  0.69206852])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
