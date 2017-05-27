#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E32.4283701514_hkl-2.04028680681,-1.66242489441,-1.53903927422/sample/sampleassembly.xml'
psi = -0.0023014223711990264
hkl2Q = array([[-0.65852848,  0.93586142,  0.        ],
       [ 0.66175396,  0.46564996, -0.80916512],
       [-0.66175396, -0.46564996, -0.80916512]])
pp = array([ 2.94089404,  0.59257258, -0.78045782])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.002446365961372965
Q = array([ 1.26193606, -1.96688023,  2.59051313])
E = 32.428370151393381
hkl_projection = array([-0.57279647, -0.65133347, -0.87169757])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
