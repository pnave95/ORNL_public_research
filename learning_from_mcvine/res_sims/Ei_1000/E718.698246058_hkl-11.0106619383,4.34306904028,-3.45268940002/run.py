#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E718.698246058_hkl-11.0106619383,4.34306904028,-3.45268940002/sample/sampleassembly.xml'
psi = -0.010054377754225635
hkl2Q = array([[-0.65125307,  0.94093879,  0.        ],
       [ 0.6653442 ,  0.46050546, -0.80916512],
       [-0.6653442 , -0.46050546, -0.80916512]])
pp = array([ 2.46255016,  1.71343127,  0.18233359])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0013849084427826485
Q = array([ 12.35759008,  -6.77036955,  -0.72046415])
E = 718.69824605804934
hkl_projection = array([-0.93531817, -0.20923308,  0.98447002])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
