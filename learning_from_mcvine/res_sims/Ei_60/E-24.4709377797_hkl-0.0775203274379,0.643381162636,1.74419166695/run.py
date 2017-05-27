#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-24.4709377797_hkl-0.0775203274379,0.643381162636,1.74419166695/sample/sampleassembly.xml'
psi = 0.00546473879793744
hkl2Q = array([[-0.6657766 ,  0.93071902,  0.        ],
       [ 0.65811773,  0.47077515, -0.80916512],
       [-0.65811773, -0.47077515, -0.80916512]])
pp = array([ 2.98595419,  0.28996136,  0.94885405])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0048009306765405399
Q = array([-0.67285169, -0.59038387, -1.93194065])
E = -24.470937779691397
hkl_projection = array([ 0.27735408,  0.26154899,  0.40406191])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
