#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E4.22086022673_hkl-3.20545001488,0.129995263837,0.977548208487/sample/sampleassembly.xml'
psi = -0.00218441495382745
hkl2Q = array([[-0.65863798,  0.93578437,  0.        ],
       [ 0.66169947,  0.46572738, -0.80916512],
       [-0.66169947, -0.46572738, -0.80916512]])
pp = array([ 2.25193016,  1.98212274,  0.52332721])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.00494833541754954
Q = array([ 1.5504058 , -3.39433862, -0.89618554])
E = 4.2208602267291013
hkl_projection = array([ 0.51683214, -0.38485472,  0.68909229])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
