#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-826.157540337_hkl4.93926453878,-5.44415163941,0.879245539097/sample/sampleassembly.xml'
psi = -0.023124046233718533
hkl2Q = array([[-0.63890004,  0.94936985,  0.        ],
       [ 0.67130586,  0.45177055, -0.80916512],
       [-0.67130586, -0.45177055, -0.80916512]])
pp = array([ 2.99422439, -0.18606529, -0.37505838])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011442248315937172
Q = array([-7.40062989,  1.83246417,  3.69376278])
E = -826.15754033725648
hkl_projection = array([-0.05060242,  0.57720016,  0.53745456])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
