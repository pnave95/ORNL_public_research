#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-33.2959215671_hkl0.0959820877027,0.22897871617,1.42993041249/sample/sampleassembly.xml'
psi = 0.008679020556656519
hkl2Q = array([[-0.66876475,  0.92857422,  0.        ],
       [ 0.65660113,  0.47288809, -0.80916512],
       [-0.65660113, -0.47288809, -0.80916512]])
pp = array([ 2.99542246,  0.1656631 ,  0.46445233])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0033333020580882475
Q = array([-0.85273567, -0.47878926, -1.3423314 ])
E = -33.295921567087632
hkl_projection = array([-0.87422754, -0.72735992, -0.12060033])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
