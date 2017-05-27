#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E192.68894192_hkl-4.74716577077,2.77897044689,-1.95616586598/sample/sampleassembly.xml'
psi = -0.00992506940426267
hkl2Q = array([[-0.65137474,  0.94085457,  0.        ],
       [ 0.66528465,  0.4605915 , -0.80916512],
       [-0.66528465, -0.4605915 , -0.80916512]])
pp = array([ 2.70665509,  1.29383855,  0.3769174 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0028670146895241931
Q = array([ 6.24239735, -2.28542909, -0.66578476])
E = 192.68894191995236
hkl_projection = array([-0.51423184,  0.52444659,  0.03742423])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
