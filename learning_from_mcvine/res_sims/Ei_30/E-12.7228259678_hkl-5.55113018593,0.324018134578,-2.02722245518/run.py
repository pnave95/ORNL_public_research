#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-12.7228259678_hkl-5.55113018593,0.324018134578,-2.02722245518/sample/sampleassembly.xml'
psi = -0.004709462357663993
hkl2Q = array([[-0.65627299,  0.93744447,  0.        ],
       [ 0.66287334,  0.46405508, -0.80916512],
       [-0.66287334, -0.46405508, -0.80916512]])
pp = array([-0.95589637,  2.84363537, -0.95289108])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0067862915959182504
Q = array([ 5.20163149, -4.11277117,  1.37817352])
E = -12.722825967783242
hkl_projection = array([ 0.54065414, -0.72612404, -0.53360338])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
