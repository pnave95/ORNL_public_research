#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-548.600659036_hkl-11.3850932427,-7.34340419093,4.11746944556/sample/sampleassembly.xml'
psi = 1.6994587788869183e-05
hkl2Q = array([[-0.66069643,  0.93433217,  0.        ],
       [ 0.66067261,  0.46718293, -0.80916512],
       [-0.66067261, -0.46718293, -0.80916512]])
pp = array([ 2.43186134,  1.7567158 , -0.28674598])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011574277647546057
Q = array([ -0.04979486, -15.99178332,   2.61031386])
E = -548.60065903645364
hkl_projection = array([ 0.24747562,  0.4019668 , -0.49200441])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
