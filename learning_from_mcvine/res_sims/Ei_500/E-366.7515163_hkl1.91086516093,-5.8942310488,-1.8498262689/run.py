#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-366.7515163_hkl1.91086516093,-5.8942310488,-1.8498262689/sample/sampleassembly.xml'
psi = 0.07440083566345529
hkl2Q = array([[-0.72830461,  0.88264872,  0.        ],
       [ 0.62412689,  0.51498913, -0.80916512],
       [-0.62412689, -0.51498913, -0.80916512]])
pp = array([ 2.99938245,  0.06086806, -0.9626728 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016347659888644997
Q = array([-3.91591371, -0.39620182,  6.26622104])
E = -366.75151630018161
hkl_projection = array([-0.33801017, -0.77684417, -0.40965621])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
