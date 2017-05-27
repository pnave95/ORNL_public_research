#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E24.7434826427_hkl-13.0507814706,2.34262208795,-1.49264209719/sample/sampleassembly.xml'
psi = -0.00382268481261648
hkl2Q = array([[-0.65710403,  0.93686214,  0.        ],
       [ 0.66246157,  0.46464272, -0.80916512],
       [-0.66246157, -0.46464272, -0.80916512]])
pp = array([-0.02671628,  2.99988104,  0.19753844])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0024240330674112102
Q = array([ 11.11643626, -10.44475544,  -0.68777416])
E = 24.743482642661036
hkl_projection = array([-0.74938104,  0.01227732,  0.25644459])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
