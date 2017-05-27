#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-23.0800041944_hkl-3.30129735491,-1.78436922034,0.0634072135788/sample/sampleassembly.xml'
psi = -0.0008996489180258688
hkl2Q = array([[-0.6598397 ,  0.9349374 ,  0.        ],
       [ 0.66110057,  0.46657713, -0.80916512],
       [-0.66110057, -0.46657713, -0.80916512]])
pp = array([ 1.76073694,  2.42895151, -0.85660403])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0066651408769540302
Q = array([ 0.956761  , -3.94863658,  1.39254242])
E = -23.080004194364239
hkl_projection = array([ 0.61750512, -0.01135121, -0.16490089])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
