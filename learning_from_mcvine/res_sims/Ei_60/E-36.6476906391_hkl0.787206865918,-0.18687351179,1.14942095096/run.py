#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-36.6476906391_hkl0.787206865918,-0.18687351179,1.14942095096/sample/sampleassembly.xml'
psi = -0.04642519329658169
hkl2Q = array([[-0.6166072 ,  0.96399789,  0.        ],
       [ 0.68164944,  0.43600714, -0.80916512],
       [-0.68164944, -0.43600714, -0.80916512]])
pp = array([ 2.99899392, -0.07768825,  0.34334463])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047210246834178743
Q = array([-1.3962818 ,  0.17623183, -0.77885981])
E = -36.64769063913576
hkl_projection = array([ 0.24549431, -0.35642556,  0.66687696])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
