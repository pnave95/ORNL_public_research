#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E50.0478359024_hkl-2.70807429946,1.19280160011,-1.55263547454/sample/sampleassembly.xml'
psi = -0.0134761174699825
hkl2Q = array([[-0.64802962,  0.9431617 ,  0.        ],
       [ 0.66691603,  0.45822614, -0.80916512],
       [-0.66691603, -0.45822614, -0.80916512]])
pp = array([ 2.44406552,  1.73969645, -0.39081134])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0061526829727257312
Q = array([ 3.58588835, -1.29612092,  0.29116502])
E = 50.047835902419649
hkl_projection = array([-0.13619394, -0.10250639, -0.23438431])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
