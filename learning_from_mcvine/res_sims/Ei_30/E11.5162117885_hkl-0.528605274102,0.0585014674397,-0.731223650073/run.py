#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E11.5162117885_hkl-0.528605274102,0.0585014674397,-0.731223650073/sample/sampleassembly.xml'
psi = -0.023807919947113572
hkl2Q = array([[-0.63825065,  0.94980655,  0.        ],
       [ 0.67161465,  0.45131136, -0.80916512],
       [-0.67161465, -0.45131136, -0.80916512]])
pp = array([ 2.99635291,  0.14788252, -0.55264589])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0073006266015605004
Q = array([ 0.86777362, -0.14566084,  0.54434332])
E = 11.516211788462812
hkl_projection = array([ 0.29467558, -0.02263544,  0.34422156])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
