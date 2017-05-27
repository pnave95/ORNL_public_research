#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-6.29292099041_hkl-4.31468966098,-0.366089452776,-0.365876696846/sample/sampleassembly.xml'
psi = -0.0026128376023309232
hkl2Q = array([[-0.65823701,  0.93606646,  0.        ],
       [ 0.66189894,  0.46544385, -0.80916512],
       [-0.66189894, -0.46544385, -0.80916512]])
pp = array([ 0.70681914,  2.91554569, -0.42754429])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0068346445422717761
Q = array([ 2.8399476 , -4.03893528,  0.59228147])
E = -6.2929209904101526
hkl_projection = array([ 0.09783524, -0.84921824, -0.41518094])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
