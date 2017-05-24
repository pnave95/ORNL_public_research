#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-3.11457745147_hkl-3.20130195655,-0.0751236137784,0.645822298857/sample/sampleassembly.xml'
psi = -0.001820531502729238
hkl2Q = array([[-0.65897846,  0.93554464,  0.        ],
       [ 0.66152996,  0.46596813, -0.80916512],
       [-0.66152996, -0.46596813, -0.80916512]])
pp = array([ 1.64625742,  2.50795465,  0.34769807])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0068840017317576075
Q = array([ 1.6326617 , -3.3308987 , -0.46178947])
E = -3.1145774514732416
hkl_projection = array([-0.20243322, -0.38216986,  0.45612727])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
