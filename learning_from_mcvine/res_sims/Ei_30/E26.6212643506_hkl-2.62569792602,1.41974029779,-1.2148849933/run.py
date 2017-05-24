#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E26.6212643506_hkl-2.62569792602,1.41974029779,-1.2148849933/sample/sampleassembly.xml'
psi = -0.010362842663599011
hkl2Q = array([[-0.6509628 ,  0.94113963,  0.        ],
       [ 0.66548622,  0.46030021, -0.80916512],
       [-0.66548622, -0.46030021, -0.80916512]])
pp = array([ 0.81784551,  2.88636947,  0.38019578])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0093310123957296293
Q = array([ 3.46253848, -1.25842981, -0.16576177])
E = 26.621264350637212
hkl_projection = array([-0.50539924, -0.08983528, -0.19249424])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
