#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E283.058782047_hkl-3.53427182384,4.44902453853,-0.769394747283/sample/sampleassembly.xml'
psi = -0.028873158004339722
hkl2Q = array([[-0.63343148,  0.95302724,  0.        ],
       [ 0.67389203,  0.4479037 , -0.80916512],
       [-0.67389203, -0.4479037 , -0.80916512]])
pp = array([ 2.98371041,  0.31220535,  0.9016992 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0018717591555596543
Q = array([ 5.75537019, -1.03090805, -2.97742807])
E = 283.05878204733619
hkl_projection = array([-0.9561532 ,  0.00591973, -0.65138158])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
