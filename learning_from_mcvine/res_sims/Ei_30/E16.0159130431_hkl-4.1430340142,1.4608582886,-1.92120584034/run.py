#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E16.0159130431_hkl-4.1430340142,1.4608582886,-1.92120584034/sample/sampleassembly.xml'
psi = -0.007958055936116629
hkl2Q = array([[-0.65322415,  0.93957149,  0.        ],
       [ 0.66437737,  0.46189923, -0.80916512],
       [-0.66437737, -0.46189923, -0.80916512]])
pp = array([-1.31279656,  2.69751093, -0.43115793])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0075265197786447482
Q = array([ 4.95329675, -2.33050382,  0.37249718])
E = 16.015913043093569
hkl_projection = array([-0.78035283,  0.81501556, -0.53275618])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
