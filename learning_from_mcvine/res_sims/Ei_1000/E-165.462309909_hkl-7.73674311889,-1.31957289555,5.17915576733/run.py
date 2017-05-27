#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-165.462309909_hkl-7.73674311889,-1.31957289555,5.17915576733/sample/sampleassembly.xml'
psi = -0.00043253230082241864
hkl2Q = array([[-0.66027636,  0.93462907,  0.        ],
       [ 0.66088256,  0.46688589, -0.80916512],
       [-0.66088256, -0.46688589, -0.80916512]])
pp = array([ 2.70191831,  1.30370145,  0.3966344 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011846687532208904
Q = array([  0.81349214, -10.26514976,  -3.12303982])
E = -165.46230990858817
hkl_projection = array([ 0.24980024,  0.74426713, -0.343835  ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
