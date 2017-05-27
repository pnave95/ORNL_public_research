#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E34.5467412048_hkl-6.45879947415,-0.114074495012,-0.659776578787/sample/sampleassembly.xml'
psi = -0.0038469752645607642
hkl2Q = array([[-0.65708128,  0.9368781 ,  0.        ],
       [ 0.66247286,  0.46462663, -0.80916512],
       [-0.66247286, -0.46462663, -0.80916512]])
pp = array([ 1.44934537,  2.62667051, -0.28369709])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0035033415934893936
Q = array([ 4.60546901, -5.79756004,  0.62617329])
E = 34.546741204836792
hkl_projection = array([ 0.50687814,  0.19413011, -0.4410174 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
