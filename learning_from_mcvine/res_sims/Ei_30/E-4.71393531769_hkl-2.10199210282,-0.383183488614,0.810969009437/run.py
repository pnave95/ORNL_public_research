#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-4.71393531769_hkl-2.10199210282,-0.383183488614,0.810969009437/sample/sampleassembly.xml'
psi = -0.0008796195941166206
hkl2Q = array([[-0.65985843,  0.93492418,  0.        ],
       [ 0.66109123,  0.46659037, -0.80916512],
       [-0.66109123, -0.46659037, -0.80916512]])
pp = array([ 2.36209513,  1.84946117,  0.25380336])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0068526867175326698
Q = array([ 0.59757346, -2.5223833 , -0.34614912])
E = -4.7139353176891277
hkl_projection = array([ 0.87613158, -0.77573293, -0.02220635])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
