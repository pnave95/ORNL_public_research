#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E79.6968332191_hkl-19.1338317556,2.61577150719,-7.69367015464/sample/sampleassembly.xml'
psi = -0.007010642910180349
hkl2Q = array([[-0.65411402,  0.93895219,  0.        ],
       [ 0.66393946,  0.46252846, -0.80916512],
       [-0.66393946, -0.46252846, -0.80916512]])
pp = array([-0.82057342,  2.88559513, -0.89840067])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017380355591821448
Q = array([ 19.36055278, -13.1973431 ,   4.10885845])
E = 79.696833219100768
hkl_projection = array([-0.18862116,  0.99704682,  0.8107622 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
