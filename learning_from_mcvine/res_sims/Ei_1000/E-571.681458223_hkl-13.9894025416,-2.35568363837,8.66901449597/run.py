#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-571.681458223_hkl-13.9894025416,-2.35568363837,8.66901449597/sample/sampleassembly.xml'
psi = -0.0005834965941194309
hkl2Q = array([[-0.66013525,  0.93472874,  0.        ],
       [ 0.66095303,  0.46678611, -0.80916512],
       [-0.66095303, -0.46678611, -0.80916512]])
pp = array([ 2.22457124,  2.01277987,  0.56426703])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.001158388282401555
Q = array([  1.94809012, -18.22247262,  -5.1085271 ])
E = -571.68145822280917
hkl_projection = array([ 0.13831352, -0.506466  ,  0.35906032])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
