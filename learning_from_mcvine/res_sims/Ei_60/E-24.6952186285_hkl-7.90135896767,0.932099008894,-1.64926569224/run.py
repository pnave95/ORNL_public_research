#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-24.6952186285_hkl-7.90135896767,0.932099008894,-1.64926569224/sample/sampleassembly.xml'
psi = -0.005318377357175326
hkl2Q = array([[-0.65570204,  0.93784391,  0.        ],
       [ 0.66315579,  0.46365136, -0.80916512],
       [-0.66315579, -0.46365136, -0.80916512]])
pp = array([-0.69780432,  2.91771642, -0.27250335])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047666958980605439
Q = array([ 6.89278414, -6.21338817,  0.58030626])
E = -24.6952186284514
hkl_projection = array([-0.68074873, -0.90277604,  0.72217419])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
