#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E13.2677077909_hkl-1.34335602536,0.58886861211,0.0959729015355/sample/sampleassembly.xml'
psi = -0.004367041230727218
hkl2Q = array([[-0.65659395,  0.9372197 ,  0.        ],
       [ 0.6627144 ,  0.46428203, -0.80916512],
       [-0.6627144 , -0.46428203, -0.80916512]])
pp = array([ 2.79055801,  1.10126562,  0.59238959])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0073860011250041682
Q = array([ 1.20868852, -1.0301771 , -0.55414986])
E = 13.267707790931134
hkl_projection = array([-0.75314568, -0.33980141,  0.23092727])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
