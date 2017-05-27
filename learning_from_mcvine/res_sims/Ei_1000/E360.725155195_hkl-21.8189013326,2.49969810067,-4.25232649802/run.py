#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E360.725155195_hkl-21.8189013326,2.49969810067,-4.25232649802/sample/sampleassembly.xml'
psi = -0.0059269940148820215
hkl2Q = array([[-0.65513113,  0.93824281,  0.        ],
       [ 0.66343785,  0.46324767, -0.80916512],
       [-0.66343785, -0.46324767, -0.80916512]])
pp = array([ 0.56308475,  2.94668213, -0.24094718])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012528015597677996
Q = array([ 18.77379022, -17.34356769,   1.41816576])
E = 360.72515519485296
hkl_projection = array([ 0.73408283, -0.45212701,  0.83131483])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
