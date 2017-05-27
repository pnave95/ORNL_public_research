#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E330.611832756_hkl-14.8597790253,4.7005001135,-6.02875318831/sample/sampleassembly.xml'
psi = -0.008940930627240693
hkl2Q = array([[-0.65230036,  0.94021307,  0.        ],
       [ 0.66483104,  0.461246  , -0.80916512],
       [-0.66483104, -0.461246  , -0.80916512]])
pp = array([-0.40152045,  2.9730088 , -0.35414873])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0019141088971679292
Q = array([ 16.82617975,  -9.02253324,   1.07477605])
E = 330.61183275595249
hkl_projection = array([-0.90348946,  0.82608953, -0.33405121])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
